from distutils.core import setup

setup(
    name='plotly_svg',
    packages=['plotly_svg'],
    version='0.01',
    license='BSD0',
    description='Convenient way of generating vector graphics from plotly offline',
    author='tech2077',
    author_email='tech2077@gmail.com',
    url='https://github.com/user/reponame',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
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
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
