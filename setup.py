#!/usr/bin/env python

import setuptools
from ESICelery import __version__


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(name='ESICelery',
                 version=__version__,
                 description='ESI celery task queues for distributed API access using RabbitMQ and Redis.',
                 license="GNU General Public License v3.0",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author_email='maintainers@eveinsight.net',
                 url='https://github.com/EVEInsight/ESICelery',
                 packages=setuptools.find_packages(include=["ESICelery", "ESICelery.*"]),
                 install_requires=[
                       'Celery>=5.2,<6',
                       'python-dateutil>=2.8.2,<3',
                       'redis>=4.1,<5',
                       'requests>=2.27,<3'
                 ],
                 python_requires=">=3.7"
                 )
