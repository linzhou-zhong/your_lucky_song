#! /usr/bin/env python
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

with open('requirements_test.txt') as f:
    requirements_test = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name="your_day_song",
        version="1.0",
        description="A python package for finding song on the day you were born",
        long_description=long_description,
        author="Linzhou ZHONG",
        author_email="justgiveacar@gmail.com",
        license="",
        url="",
        install_requires=install_requires,
        tests_require=requirements_test,
        packages=find_packages(),
    )
