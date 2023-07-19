import os

from setuptools import setup

_this = os.path.abspath(os.path.dirname(__file__))


def get_requirements(filename):
    contents = open(os.path.join(_this, filename)).read()
    return [
        req for req in contents.split("\n") if req != "" and not req.startswith("#")
    ]


setup(
    version="0.1.4",
    install_requires=get_requirements("requirements.txt"),
)
