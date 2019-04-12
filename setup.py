from distutils.core import setup

setup(
    name='plotly_svg',
    packages=['plotly_svg'],
    version='0.01',
    license='0BSD',
    description='Convenient way of generating vector graphics from plotly offline',
    author='tech2077',
    author_email='tech2077@gmail.com',
    url='https://github.com/tech2077/plotly_svg',
    download_url='https://github.com/tech2077/plotly_svg/archive/v_01.tar.gz',
    keywords=['plotly', 'svg', 'pdf'],
    install_requires=[
        'plotly',
        'cairosvg',
        'pyppeteer'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
