************
`plotly_svg`
************

[![image](https://img.shields.io/pypi/v/plotly-svg.svg)](https://pypi.org/project/plotly-svg/)
[![image](https://img.shields.io/pypi/l/plotly-svg.svg)](https://pypi.org/project/plotly-svg/)
[![image](https://img.shields.io/pypi/pyversions/plotly-svg.svg)](https://pypi.org/project/plotly-svg/)

Convenient way of generating vector graphics from plotly offline

The main reason for this package's existence is a frustration
with plotly's existing tool orca. While orca works perfectly
fine in desktop environments, it's incredibly frustrating to
work with in headless environments, especially without access
to root or a package manager (jupyter notebook services, school
computers, etc.).

Installation
============
`plotly_svg` can be installed from PyPI using `pip`::

    pip install plotly_svg


Usage
=====
::

    from plotly_svg import to_svg, to_pdf

    ## to save to svg
    to_svg(plotly_fig, file="figure.svg")

    ## to save to pdf
    to_pdf(plotly_fig, file="figure.pdf")

    ## load svg to string
    svg_str = to_svg(plotly_fig, output_type="str")

    ## load pdf to string
    pdf_bytes = to_pdf(plotly_fig, output_type="str")

