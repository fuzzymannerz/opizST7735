from setuptools import setup, find_packages
import sys

if sys.version_info < (3, 3, 0):
    raise RuntimeError("This library requires Python 3.3.0+")

setup(
    name="opiz ST7735",
    version="1.0",
    description="Python library for using ST7735-based TFT LCDs with an Orange Pi Zero",
    url="https://github.com/fuzzymannerz/opizST7735",
    author="Fuzzy",
    license="MIT",
    install_requires = [
        'OPi.GPIO>=0',
        'spidev>=3.0',
        'Pillow>=4.2.0'
    ],
    packages=find_packages()
)
