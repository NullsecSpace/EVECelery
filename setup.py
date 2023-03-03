#!/usr/bin/env python

import setuptools

pkg_info = {}
with open("ESICelery/__version__.py", "r", encoding="utf-8") as f:
    for l in f.readlines():
        data = l.split('=')
        pkg_info[data[0].strip()] = (data[1].replace("'", "")).strip()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt', "r", encoding="utf-8") as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='ESICelery',
                 version=pkg_info['__version__'],
                 description=pkg_info['__description__'],
                 license=pkg_info['__license__'],
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author_email=pkg_info['__author_email__'],
                 url=pkg_info['__url__'],
                 packages=setuptools.find_packages(include=["ESICelery", "ESICelery.*"]),
                 install_requires=install_requires,
                 python_requires=">=3.7"
                 )
