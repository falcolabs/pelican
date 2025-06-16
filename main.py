import PIL.Image
import aiohttp
import asyncio
import pytesseract
import cv2
import numpy as np
import base64
import PIL
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from io import BytesIO
from timeit import default_timer as timer

ua = UserAgent()
CAPTCHA_ID, CAPTCHA = "", ""


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
    CAPTCHA_ID = captchaID
    CAPTCHA = captcha


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
        return await r.json()


async def lookup(session: aiohttp.ClientSession, sbd: str) -> dict:
    print(f"[*] lookup {sbd}")
    token = await extract_token(session)
    tries = 0
    while tries < 3:
        info = await get_info(session, sbd, token, CAPTCHA_ID, CAPTCHA)
        if info["message"] == "Sai mã bảo vệ.":
            print(f"  [-] attempt #{tries+1}: wrong captcha.")
            await refresh_captcha(session)
        else:
            print(f"  [+] attempt #{tries+1}: success")
            return info
        tries += 1
    print(f"  [!] tried 3 times, giving up on {sbd}")
    with open("failed.txt", "a") as f:
        f.write(f"{sbd}\n")
        return {}


async def main():
    async with aiohttp.ClientSession() as session:
        await refresh_captcha(session)
        print(await lookup(session, "023452"))


asyncio.run(main())
