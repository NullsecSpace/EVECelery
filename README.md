# EVECelery

[![PyPI](https://img.shields.io/pypi/v/EVECelery)](https://pypi.org/project/EVECelery)
[![Documentation Status](https://readthedocs.org/projects/evecelery/badge/?version=latest)](https://evecelery.nullsec.space/en/latest/?badge=latest)
[![EVECelery](https://github.com/NullsecSpace/EVECelery/actions/workflows/github-actions.yml/badge.svg)](https://github.com/NullsecSpace/EVECelery/actions/workflows/github-actions.yml)
[![GitHub](https://img.shields.io/github/license/NullsecSpace/EVECelery)](https://github.com/NullsecSpace/EVECelery/blob/main/LICENSE)

EVECelery is a distributed task queue framework for building tools that interact with
the [EVE Online ESI API](https://esi.evetech.net/ui) using Celery, RabbitMQ, and Redis.

With EVECelery you can easily distribute ESI calls across task queues built on top
of [Celery](https://docs.celeryq.dev/) with a fleet of worker nodes.
You can build on top of EVECelery to create your own tools defining custom tasks and scheduled jobs.

NOTE: This software is in development and may rapidly change or have breaking bugs until the v1.0 release is ready.
Ensure you use version pinning in your ```requirements.txt```.

- :books: Documentation: https://evecelery.nullsec.space
- :bulb: Examples: https://evecelery.nullsec.space/en/latest/examples/index.html

# Installation

```
pip install EVECelery
```

# Requirements

EVECelery requires RabbitMQ for the message broker service and Redis for distributed locks, cache, and Celery's result
backend (fetching the result of completed tasks).

Deploying these two servers through the official Docker images for [RabbitMQ](https://hub.docker.com/_/rabbitmq)
and [Redis](https://hub.docker.com/_/redis) is recommended.

# Quickstart and Usage
EVECelery has two components:
* Celery Worker - The Celery worker server that processes tasks from the message broker and makes requests to ESI on behalf of the client applications 
* Task api - Collection of Celery tasks to make ESI requests from your client application

You can deploy multiple worker servers that process tasks in the message queues. These worker nodes share locks, error limiting info, and cache requests for clients.
From your application you make requests using the task api.


## Starting the Celery Worker
You can start the worker server from either the CLI or your own Python script.
It is recommended to use the CLI unless you plan on registering your own tasks to the celery worker.

### From CLI

Ensure the following environmental variables are set and run the application via bash:
* EVECelery_RabbitMQ_User
* EVECelery_RabbitMQ_Password
* EVECelery_RabbitMQ_Host
* EVECelery_RabbitMQ_Port
* EVECelery_RabbitMQ_Vhost
* EVECelery_Redis_ResultBackend_User
* EVECelery_Redis_ResultBackend_Password
* EVECelery_Redis_ResultBackend_Host
* EVECelery_Redis_ResultBackend_Port
* EVECelery_Redis_ResultBackend_DB
* EVECelery_Email

```shell
$ eve-celery
```

### From your code
You can also start the worker from a Python script if you don't want to set environmental variables.

```python

from EVECelery import EVECeleryWorker

c = EVECeleryWorker(broker_user="user", broker_password="pass", broker_host="host", broker_port=5672,
                    broker_vhost="esi",
                    result_user="user", result_password="pass", result_host="host", result_port=6379, result_db=0)

c.start()
```

## Using the task API from your code
From another Python script you can send tasks to the queues and receive results:

```python

from EVECelery import EVECeleryWorker
from EVECelery.tasks.Universe import SystemInfo

# only need to make one CeleryWorker in our code to init the tasks and setup connections to RabbitMQ and Redis
# by not passing connection params to CeleryWorker() the connection info will be read from environmental variables
c = EVECeleryWorker()

# note we don't call c.start() here as this is not a worker node script.
# we are calling the task api to submit requests to the message queue which run on the Celery worker nodes

r = SystemInfo().get_sync(timeout=5, system_id=30000142)
# r is a response dictionary containing system info obtained from ESI.
# subsequent calls for the same system ID will return results from the cache regardless of requesting client
```

# Copyright Notice

See [CCP.md](https://github.com/NullsecSpace/EVECelery/blob/main/CCP.md)

