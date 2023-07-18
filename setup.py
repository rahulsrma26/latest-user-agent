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
    name="latest_user_agent",
    version="0.1.0",
    url="https://github.com/rahulsrma26/latest-user-agent",
    license="MIT",
    author="Rahul Sharma",
    author_email="welcometors@gmail.com",
    description="A small package to generate user-agents",
    long_description=read("README.rst"),
    packages=find_packages(exclude=("tests",)),
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
