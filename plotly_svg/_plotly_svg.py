import asyncio
import cairosvg
import re
from typing import Union, TextIO
from plotly.offline import plot
from pyppeteer import launch


async def extract_svg_all_runner(fig):
    """Pull out all svg content in plotly html output

    :param fig: Plotly Figure (figure object or dict)
    :return: list of str containing all svg chunks in html
    """

    # get plot html
    out = plot(fig, output_type="div")

    # generate a valid html page to load
    html = ''.join(['<html>', '<head><meta charset="utf-8" /></head>', '<body>', out, '</body>', '</html>'])

    # start headless chromium and open a new page
    browser = await launch(headless=True)
    page = await browser.newPage()

    # load plot html page and wait for render, then read back rendered page
    await page.setContent(html)
    rendered_content = await page.content()

    # match all svg content in page
    # yes, I know you can't parse html with regex, this
    # is a special case with a verified source document
    # and it's finding, not parsing
    matches = re.findall(r"<svg.*?</svg>", rendered_content)

    # cleanup and return
    await browser.close()
    return matches


async def extract_svg_runner(fig):
    """Pull out all MAIN svg content in plotly html output

    :param fig: Plotly Figure (figure object or dict)
    :return: svg string
    """

    # get plot html
    out = plot(fig, output_type="div")

    # generate a valid html page to load
    html = ''.join(['<html>', '<head><meta charset="utf-8" /></head>', '<body>', out, '</body>', '</html>'])

    # start headless chromium and open a new page
    browser = await launch(headless=True)
    page = await browser.newPage()

    # load plot html page and wait for render, then read back rendered page
    await page.setContent(html)
    rendered_content = await page.content()

    # match main (figure) svg content in page
    # yes, I know you can't parse html with regex, this
    # is a special case with a verified source document
    # and it's finding, not parsing
    matches = re.findall(r'<svg class="main.*?</svg>', rendered_content)

    await browser.close()

    # return a single svg, constructed from two svgs on page
    # one svg contains graph labels and legend, other svg contains
    # graph content. Ugly hack to combine, but it works
    return matches[0][0:-6] + re.sub(r"<svg.*?>", "", matches[1])


def to_svg(fig, file: Union[str, TextIO] = "out.svg", output_type: str = "file"):
    """Generate SVG from plotly figure

    :param fig: Plotly Figure (figure object or dict)
    :param file: filename or file object
    :param output_type: either "file" or str" to specify file or string output
    :return: returns either None or svg string
    """

    # get svg string from headless render
    svg_str = asyncio.get_event_loop().run_until_complete(extract_svg_runner(fig))

    # output logic
    if output_type == "file":
        if type(file) == str:
            with open(file, "w") as f:
                f.write(svg_str)
        else:
            file.write(svg_str)
    elif output_type == "str":
        return svg_str


def to_pdf(fig, file: Union[str, TextIO] = "out.pdf", output_type: str = "file"):
    """Generate pdf from plotly figure

    :param fig: Plotly Figure (figure object or dict)
    :param file: filename or file object
    :param output_type: either "file" or str" to specify file or string output
    :return: returns either None or svg string
    """

    # get svg string and convert to pdf
    svg_str = to_svg(fig, output_type="str")
    pdf_bytes = cairosvg.svg2pdf(bytestring=svg_str)

    # output logic
    if output_type == "file":
        if type(file) == str:
            with open(file, "wb") as f:
                f.write(pdf_bytes)
        else:
            file.write(pdf_bytes)
    elif output_type == "str":
        return pdf_bytes
