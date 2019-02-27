"""Metadata for pypi uploads."""
import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="stm-metro-client",
    version="0.0.4",
    author="Karim Roukoz",
    author_email="roukoz@gmail.com",
    description="A python client for Montreal's STM metro line status",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords=['montreal', 'transit', 'metro', 'subway', 'quebec'],
    url="https://github.com/kkr16/stm-metro-client",
    packages=setuptools.find_packages(),
)
