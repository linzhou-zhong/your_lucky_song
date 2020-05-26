#! /usr/bin/env python
from setuptools import setup, find_packages


def install_requires():
    with open('requirements.txt') as f:
        install_requires = f.read().splitlines()
    return install_requires


def requirements_test():
    with open('requirements_test.txt') as f:
        requirements_test = f.read().splitlines()
    return requirements_test


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description


if __name__ == "__main__":
    setup(
        name="your_lucky_song",
        # version="1.0",
        description="A python package for finding song on the day you were born",
        long_description=readme(),
        long_description_content_type='text/markdown',
        author="Linzhou ZHONG",
        author_email="justgiveacar@gmail.com",
        license="MIT",
        url="https://github.com/linzhou-zhong/your_lucky_song",
        install_requires=install_requires(),
        tests_require=requirements_test(),
        packages=find_packages(),
    )
