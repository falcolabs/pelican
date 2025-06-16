# Project Pelican
# Copyright (C) 2025  FalcoLabs Research
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import PIL.Image
import aiohttp
import asyncio
import pytesseract
import cv2
import numpy as np
import base64
import PIL
import os
import json
import traceback
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from io import BytesIO
from timeit import default_timer as timer

ua = UserAgent()
CAPTCHA_ID, CAPTCHA = "", ""
RESULTS = {}


async def extract_token(session: aiohttp.ClientSession) -> str:
    async with session.get(
        "http://tsdaucap.bacninh.edu.vn/tra-cuu-ket-qua-tuyen-sinh-bac-ninh"
    ) as r:
        markup = BeautifulSoup(markup=await r.text(), features="html.parser")
        token = markup.find("input", {"name": "__RequestVerificationToken"}).attrs[  # type: ignore
            "value"
        ]
        return str(token)


def solve_captcha(captchab64: str) -> str:
    inp = PIL.Image.open(BytesIO(base64.b64decode(captchab64)))
    bg_filled = PIL.Image.new("RGBA", inp.size, "WHITE")
    bg_filled.paste(inp, (0, 0), inp)
    bg_filled.save("a.png")
    grayscale = cv2.cvtColor(np.array(bg_filled)[:, :, ::-1].copy(), cv2.COLOR_BGR2GRAY)
    (h, w) = grayscale.shape[:2]
    grayscale = cv2.resize(grayscale, (w * 2, h * 4))
    threshold = cv2.bitwise_not(
        cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    )
    contours = cv2.findContours(
        cv2.Canny(threshold, 30, 200), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )[0]
    contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])
    processed = np.zeros(threshold.shape, dtype=np.uint8)
    bb = cv2.boundingRect(contours[0])
    newY = bb[1] + bb[3]
    for c in contours:
        [x, y, w, h] = cv2.boundingRect(c)
        processed[newY - h : newY, x : x + w] = threshold[y : y + h, x : x + w].copy()

    return pytesseract.image_to_string(
        processed,
        config="--oem 1 --psm 10 -c tessedit_char_whitelist=ABCDEFJHIJKLMNOPQRSTUVWXYZ1234567890",
    ).strip()


async def refresh_captcha(session: aiohttp.ClientSession):
    captchaID, captcha_b64 = await extract_captcha(session)
    captcha = solve_captcha(captcha_b64)

    global CAPTCHA_ID, CAPTCHA
    CAPTCHA_ID, CAPTCHA = captchaID, captcha
    # return captchaID, captcha


async def extract_captcha(session: aiohttp.ClientSession):
    async with session.get("http://tsdaucap.bacninh.edu.vn/getcaptcha") as r:
        return (await r.json()).values()  # type: ignore


async def get_info(
    session: aiohttp.ClientSession, sbd: str, token: str, captchaID: str, captcha: str
) -> dict:
    async with session.post(
        url="http://tsdaucap.bacninh.edu.vn/tra-cuu-ket-qua-tuyen-sinh-10-bac-ninh",
        headers={
            "Requestverificationtoken": token,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": ua.random,
        },
        data=f"MA_CAP_HOC=04&MA_HOC_SINH={sbd}&CaptchaTime={captchaID}&CaptchaInput={captcha}",
    ) as r:
        try:
            return await r.json()
        except:
            session.cookie_jar.clear()
            session.headers.clear()
            await refresh_captcha(session)
            return {"ERROR": f"ERROR: {await r.content.read()}"}


def or_zero(a) -> float:
    if a == "":
        return 0.0
    return float(a)


async def lookup(
    session: aiohttp.ClientSession, sbd: str, captchaID: str = "", captcha: str = ""
) -> dict:
    global RESULTS
    token = await extract_token(session)
    tries = 0
    while tries < 10:
        info = {}
        try:
            info = await get_info(session, sbd, token, CAPTCHA_ID, CAPTCHA)
            if info["message"] == "Sai mã bảo vệ.":
                print(f"  [-] {sbd} attempt #{tries+1}: wrong captcha.")
            elif not info["result"]:
                print(f"  [-] {sbd} attempt #{tries+1}: {info["message"]}.")
            else:
                print(f"  [+] {sbd} attempt #{tries+1}: success")
                async with session.get(
                    f"http://tsdaucap.bacninh.edu.vn/TraCuu/KetQuaTraCuuTuyenSinh10BacNinh?key={info["key"]}"
                ) as req:
                    scrape = BeautifulSoup(await req.text(), features="html.parser")
                    rows = scrape.find_all("tr")
                    dr = []
                    for row in rows[1:]:
                        try:
                            dr.append(
                                str(
                                    list(
                                        filter(lambda x: x != "\n", list(row.children))
                                    )[1]
                                )[4:-5]
                            )
                        except IndexError:
                            pass
                    # print(dr)
                    # print(
                    #     {
                    #         "sbd": dr[0],
                    #         "name": dr[1],
                    #         "school": dr[6],
                    #         "birthdate": dr[3],
                    #         "math": or_zero(dr[16]),
                    #         "lit": or_zero(dr[10]),
                    #         "eng": or_zero(dr[13]),
                    #         "gifted": or_zero(dr[18]),
                    #         "totalNorm": or_zero(dr[17][8:-9]),
                    #         "totalGifted": or_zero(dr[19][8:-9]),
                    #     }
                    # )
                    return {
                        "sbd": dr[0],
                        "name": dr[1],
                        "school": dr[6],
                        "birthdate": dr[3],
                        "math": or_zero(dr[16]),
                        "lit": or_zero(dr[10]),
                        "eng": or_zero(dr[13]),
                        "gifted": or_zero(dr[18]),
                        "totalNorm": or_zero(dr[17][8:-9]),
                        "totalGifted": or_zero(dr[19][8:-9]),
                    }
        except:
            traceback.print_exc()
            print(list(zip(range(0, len(dr) + 1), dr)))
            print(f"  [-] {sbd} attempt FAILED #{tries+1} info", info)
            exit(1)
        await refresh_captcha(session)
        tries += 1
    print(f"  [!] tried 10 times, giving up on {sbd}")
    with open("failed.txt", "a") as f:
        f.write(f"{sbd}\n")
        return {}


async def main():
    global RESULTS
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(limit=200)
    ) as session:
        await refresh_captcha(session)
        with open(f"lists/{RESULTS['class']}.txt", "r", encoding="utf8") as f:
            response = []
            for i in f.read().strip().splitlines():
                r = await lookup(session, i.strip())
                response.append(r)
            RESULTS["result"] += sorted(
                response, key=lambda x: x["totalGifted"], reverse=True
            )
            RESULTS["candidates"] = len(RESULTS["result"])
            RESULTS["rate"] = 35 / len(RESULTS["result"])
            RESULTS["prediction"] = RESULTS["result"][34]["totalGifted"]
            with open(
                f"results/{RESULTS['class']}.json", "w", encoding="utf8"
            ) as resultfile:
                resultfile.write(json.dumps(RESULTS, ensure_ascii=False))


for i in os.listdir("lists"):
    RESULTS = {
        "class": i[:-4],
        "candidates": 0,
        "prediction": 50.00,
        "rate": 0,
        "result": [],
    }
    asyncio.run(main())
    print(i, f"done, writing result/{i[:-4]}.json")
