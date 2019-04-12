import asyncio
import cairosvg
import re
from typing import Union, TextIO
from plotly.offline import plot
from pyppeteer import launch


async def extract_svg_all_runner(fig):
    out = plot(fig, output_type="div")
    html = ''.join(['<html>', '<head><meta charset="utf-8" /></head>', '<body>', out, '</body>', '</html>'])
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.setContent(html)
    c = await page.content()
    matches = re.findall(r"<svg.*?</svg>", c)
    await browser.close()
    return matches


async def extract_svg_runner(fig):
    out = plot(fig, output_type="div")
    html = ''.join(['<html>', '<head><meta charset="utf-8" /></head>', '<body>', out, '</body>', '</html>'])
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.setContent(html)
    c = await page.content()
    matches = re.findall(r'<svg class="main.*?</svg>', c)
    await browser.close()
    return matches[0][0:-6] + re.sub(r"<svg.*?>", "", matches[1])


def to_svg(fig, file: Union[str, TextIO] = "out.svg", output_type: str = "file"):
    svg_str = asyncio.get_event_loop().run_until_complete(extract_svg_runner(fig))
    if output_type == "file":
        if type(file) == str:
            with open(file, "w") as f:
                f.write(svg_str)
        else:
            file.write(svg_str)
    elif output_type == "str":
        return svg_str


def to_pdf(fig, file: Union[str, TextIO] = "out.pdf", output_type: str = "file"):
    svg_str = to_svg(fig, output_type="str")
    pdf_bytes = cairosvg.svg2pdf(bytestring=svg_str)

    if output_type == "file":
        if type(file) == str:
            with open(file, "wb") as f:
                f.write(pdf_bytes)
        else:
            file.write(pdf_bytes)
    elif output_type == "str":
        return pdf_bytes
