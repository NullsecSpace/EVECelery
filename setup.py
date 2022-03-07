#!/usr/bin/env python

import setuptools

setuptools.setup(name='ESICelery',
                 version='0.6',
                 description='ESI task queues for distributed API access using RabbitMQ and Redis.',
                 author_email='maintainers@eveinsight.net',
                 url='https://github.com/EVEInsight/ESICelery',
                 packages=['ESICelery', 'ESICelery.exceptions', 'ESICelery.tasks', 'ESICelery.utils'],
                 install_requires=[
                       'Celery>=5.2,<6',
                       'python-dateutil>=2.8.2,<3',
                       'redis>=4.1,<5',
                       'requests>=2.27,<3'
                 ],
                 python_requires=">=3.10"
                 )
