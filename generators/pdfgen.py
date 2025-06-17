import os
import json
import weasyprint

CLASSDATA = {
    "van": {
        "classes": 2,
        "color": ["#EBEC94", "#A700FE"],
        "displayname": "Chuyên Văn",
        "codename": "van",
        "slogan": ["#bathoi", "#can"],
    },
    "tin": {
        "classes": 1,
        "color": "#FE0000",
        "displayname": "Chuyên Tin",
        "codename": "tin",
        "slogan": "#beit",
    },
    "ly": {
        "classes": 1,
        "color": "#3F5FFF",
        "displayname": "Chuyên Lý",
        "codename": "ly",
        "slogan": "#phily",
    },
    "hoa": {
        "classes": 1,
        "color": "#33B7C2",
        "displayname": "Chuyên Hóa",
        "codename": "hoa",
        "slogan": "#hoami",
    },
    "toan": {
        "classes": 2,
        "color": ["#109E14", "#109E14"],
        "displayname": "Chuyên Toán",
        "codename": "toan",
        "slogan": ["#toantinh", "#famash"],
    },
    "su": {
        "classes": 1,
        "color": "#754119",
        "displayname": "Chuyên Sử",
        "codename": "su",
        "slogan": "#satthat",
    },
    "dia": {
        "classes": 1,
        "color": "#6D7075",
        "displayname": "Chuyên Địa",
        "codename": "dia",
        "slogan": "#diachat",
    },
    "sinh": {
        "classes": 1,
        "color": "#FE6603",
        "displayname": "Chuyên Sinh",
        "codename": "sinh",
        "slogan": "#sinhthai",
    },
    "anh": {
        "classes": 1,
        "color": "#DA215B",
        "displayname": "Chuyên Anh",
        "codename": "anh",
        "slogan": "#pinkstorm",
    },
    "trung": {
        "classes": 1,
        "color": "#010101",
        "displayname": "Chuyên Trung",
        "codename": "trung",
        "slogan": "#rualade",
    },
    "han": {
        "classes": 1,
        "color": "#010101",
        "displayname": "Chuyên Hàn",
        "codename": "han",
        "slogan": "",
    },
}
with open("generators/template.html", "r") as f:
    TEMPLATE = f.read()

TABLE_TEMPLATE = """<tr>
    <td class="code">{stt}</td>
    <td class="code">{sbd}</td>
    <td class="left">{name}</td>
    <td class="left">{school}</td>
    <td class="code">{math}</td>
    <td class="code">{lit}</td>
    <td class="code">{eng}</td>
    <td class="code">{gifted}</td>
    <td class="code">{totalGifted}</td></tr>
"""

PAGE_BREAK = """
</table>
</div>
<div class="page-break"></div>
<div style="margin-top: 45px; background: #FFF; overflow: hidden;">
<table class="datatable">
    <tr>
        <th style="font-weight: 600; width: 5%">STT</th>
        <th style="font-weight: 600; width: inherit">SBD</th>
        <th class="left" style="font-weight: 600; width: 23%">Tên thí sinh</th>
        <th class="left" style="font-weight: 600; width: 20%">Trường</th>
        <th style="font-weight: 600; width: inherit">Toán</th>
        <th style="font-weight: 600; width: inherit">Văn</th>
        <th style="font-weight: 600; width: inherit">Anh</th>
        <th style="font-weight: 600; width: inherit">Chuyên</th>
        <th style="font-weight: 600; width: inherit">Tổng chuyên</th>
    </tr>
"""


TEMPLATE_LOGO_SINGLE = """
<div style="transform: scale(0.6) translateY(-35%); display: none;">
    <svg xmlns="http://www.w3.org/2000/svg" width="43" height="76" viewBox="0 0 43 76" fill="none">
        <g clip-path="url(#clip0_4_444)">
            <path d="M0 65.45L18.5292 55.2188L36.8287 65.5456L18.4963 76L0 65.45Z" fill=$color />
            <path d="M17.9167 11.6771L0 21.8272L0.0649154 64.125L17.9167 53.7506V11.6771Z"
                fill=$color />
            <path d="M19.9074 10.1927L37.0776 0.337173V20.0482L19.9074 10.1927Z" fill=$color />
            <path d="M36.8287 21.0781L18.912 11.2226V30.9337L36.8287 21.0781Z" fill=$color />
            <path d="M24.8842 32.9531L42.0544 23.0976V42.8087L24.8842 32.9531Z" fill=$color />
            <path d="M24.8842 54.7239L42.0544 44.8684V64.5795L24.8842 54.7239Z" fill=$color />
            <path d="M36.8287 43.3438L18.912 33.0596V53.6279L36.8287 43.3438Z" fill=$color />
        </g>
        <defs>
            <clipPath id="clip0_4_444">
                <rect width="43" height="76" fill="white" />
            </clipPath>
        </defs>
    </svg>
</div>
"""

TEMPLATE_LOGO_TWO = """
<div style="transform: scale(0.6) translateY(-35%); display: none;">
    <svg xmlns="http://www.w3.org/2000/svg" width="43" height="76" viewBox="0 0 43 76" fill="none">
        <g clip-path="url(#clip0_4_444)">
            <path d="M0 65.45L18.5292 55.2188L36.8287 65.5456L18.4963 76L0 65.45Z" fill=$color1 />
            <path d="M17.9167 11.6771L0 21.8272L0.0649154 64.125L17.9167 53.7506V11.6771Z"
                fill=$color1 />
            <path d="M19.9074 10.1927L37.0776 0.337173V20.0482L19.9074 10.1927Z" fill=$color1 />
            <path d="M36.8287 21.0781L18.912 11.2226V30.9337L36.8287 21.0781Z" fill=$color1 />
            <path d="M24.8842 32.9531L42.0544 23.0976V42.8087L24.8842 32.9531Z" fill=$color1 />
            <path d="M24.8842 54.7239L42.0544 44.8684V64.5795L24.8842 54.7239Z" fill=$color1 />
            <path d="M36.8287 43.3438L18.912 33.0596V53.6279L36.8287 43.3438Z" fill=$color1 />
        </g>
        <defs>
            <clipPath id="clip0_4_444">
                <rect width="43" height="76" fill="white" />
            </clipPath>
        </defs>
    </svg>
</div>
<div style="transform: scale(0.6) translateY(-35%); display: none;">
    <svg xmlns="http://www.w3.org/2000/svg" width="43" height="76" viewBox="0 0 43 76" fill="none">
        <g clip-path="url(#clip0_4_444)">
            <path d="M0 65.45L18.5292 55.2188L36.8287 65.5456L18.4963 76L0 65.45Z" fill=$color2 />
            <path d="M17.9167 11.6771L0 21.8272L0.0649154 64.125L17.9167 53.7506V11.6771Z"
                fill=$color2 />
            <path d="M19.9074 10.1927L37.0776 0.337173V20.0482L19.9074 10.1927Z" fill=$color2 />
            <path d="M36.8287 21.0781L18.912 11.2226V30.9337L36.8287 21.0781Z" fill=$color2 />
            <path d="M24.8842 32.9531L42.0544 23.0976V42.8087L24.8842 32.9531Z" fill=$color2 />
            <path d="M24.8842 54.7239L42.0544 44.8684V64.5795L24.8842 54.7239Z" fill=$color2 />
            <path d="M36.8287 43.3438L18.912 33.0596V53.6279L36.8287 43.3438Z" fill=$color2 />
        </g>
        <defs>
            <clipPath id="clip0_4_444">
                <rect width="43" height="76" fill="white" />
            </clipPath>
        </defs>
    </svg>
</div>
"""


def gen_table(data):
    pages = []
    output = ""
    for i, r in enumerate(data):
        output += TABLE_TEMPLATE.format(**r, stt=i + 1)
        if (len(pages) == 0 and (i + 1) % 15 == 0) or (
            len(pages) > 0 and (i + 1 - 15) % 18 == 0
        ):
            pages.append(output)
            output = ""
    pages.append(output)
    return PAGE_BREAK.join(pages)


def main():
    content = {}
    for c in os.listdir("results"):
        cn = c[:-5]
        if cn in ("td1", "ndd"):
            continue
        with open(f"results/{cn}.json", "r") as f:
            content[cn] = json.loads(f.read())

        data = CLASSDATA[cn]
        o = (
            TEMPLATE.replace("$displayname", data["displayname"])
            .replace(
                "$slogan",
                (
                    data["slogan"]
                    if isinstance(data["slogan"], str)
                    else " ".join(data["slogan"])
                ),
            )
            .replace("$candidates", str(content[data["codename"]]["candidates"]))  # type: ignore
            .replace("$prediction", f"{content[data["codename"]]["prediction"]:.2f}")  # type: ignore
            .replace("$rate", f"{(content[data["codename"]]["rate"] * 100):.2f}" + "%")  # type: ignore
            .replace("$tabledata", gen_table(content[cn]["result"]))
        )
        if isinstance(data["color"], str):
            o = (
                o.replace("$classlogo", TEMPLATE_LOGO_SINGLE)
                .replace("$color", data["color"])
                .replace("$hidehan", "display: none;" if cn == "han" else "")
            )
        else:
            o = (
                o.replace("$classlogo", TEMPLATE_LOGO_TWO)
                .replace("$color1", data["color"][0])
                .replace("$color2", data["color"][1])
                .replace("$color", "#000000")
            )
        weasyprint.HTML(string=o, base_url="./").write_pdf(f"output/{cn}.pdf")


if __name__ == "__main__":
    main()
