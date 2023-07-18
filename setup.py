import io
import os
import re

from setuptools import find_packages
from setuptools import setup

_this = os.path.abspath(os.path.dirname(__file__))


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type("")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


def get_requirements(filename):
    contents = open(os.path.join(_this, filename)).read()
    return [
        req for req in contents.split("\n") if req != "" and not req.startswith("#")
    ]


setup(
    version="0.1.3",
    long_description=read("README.rst"),
    install_requires=get_requirements('requirements.txt'),
)
