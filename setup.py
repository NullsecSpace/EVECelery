#!/usr/bin/env python

import setuptools
import ESICelery


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(name='ESICelery',
                 version=ESICelery.__version__,
                 description=ESICelery.__description__,
                 license=ESICelery.__license__,
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author_email=ESICelery.__author_email__,
                 url=ESICelery.__url__,
                 packages=setuptools.find_packages(include=["ESICelery", "ESICelery.*"]),
                 install_requires=[
                       'Celery>=5.2,<6',
                       'python-dateutil>=2.8.2,<3',
                       'redis>=4.1,<5',
                       'requests>=2.27,<3'
                 ],
                 python_requires=">=3.7"
                 )
