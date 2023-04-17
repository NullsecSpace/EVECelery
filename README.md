# EVECelery

[![PyPI](https://img.shields.io/pypi/v/EVECelery)](https://pypi.org/project/EVECelery)
[![Documentation Status](https://readthedocs.org/projects/evecelery/badge/?version=latest)](https://evecelery.nullsec.space/en/latest/?badge=latest)
[![EVECelery](https://github.com/NullsecSpace/EVECelery/actions/workflows/github-actions.yml/badge.svg)](https://github.com/NullsecSpace/EVECelery/actions/workflows/github-actions.yml)
[![GitHub](https://img.shields.io/github/license/NullsecSpace/EVECelery)](https://github.com/NullsecSpace/EVECelery/blob/main/LICENSE)

EVECelery is a distributed task queue framework for building tools that interact with
the [EVE Online ESI API](https://esi.evetech.net/ui) using Celery, RabbitMQ, and Redis.

With EVECelery you can easily distribute ESI calls and tasks across a fleet of worker nodes built using [Celery](https://docs.celeryq.dev/).
You can create your own tasks on top of EVECelery defining custom functions and scheduled jobs that run alongside the included tasks.

NOTE: This software is in development and may rapidly change or have breaking bugs until the v1.0 release is ready.
Ensure you use version pinning in your ```requirements.txt```.

- :books: Documentation: https://evecelery.nullsec.space
- :bulb: Examples: https://evecelery.nullsec.space/en/latest/examples/index.html

## Features
* Built with [Celery](https://docs.celeryq.dev/) to distribute ESI calls and tasks across a fleet of worker nodes
* Distributed locking system with Redis ensures stateless workers won't make duplicate API calls if multiple clients run tasks with matching parameters at the same time
* Cache integration with Redis that caches ESI responses
* Easily define your own Celery tasks to register with the EVECelery worker nodes
* Client support for obtaining results synchronously or asynchronously. See [Celery calling tasks](https://docs.celeryq.dev/) for docs on calling tasks.
* Automated task retry and distributed error rate control limiting across the worker fleet
* ESI task API designed to mirror the [ESI Swagger Spec](https://esi.evetech.net/ui/) with the same parameter names, responses, and documentation for easy development and code completion
* Support for periodic scheduled tasks making use of the [Celery beat scheduler](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html)

## Installation

```
pip install EVECelery
```

## Requirements

EVECelery requires RabbitMQ for the message broker service and Redis for distributed locks, cache, and Celery's result
backend (fetching the result of completed tasks).

Deploying these two servers through the official Docker images for [RabbitMQ](https://hub.docker.com/_/rabbitmq)
and [Redis](https://hub.docker.com/_/redis) is recommended.

## Quickstart and Usage
EVECelery has two components:
* Celery Worker - The Celery worker server that processes tasks from the message broker and makes requests to ESI on behalf of the client applications 
* Task api - Collection of Celery tasks to make ESI requests from your client application

You can deploy multiple worker servers that process tasks in the message queues. These worker nodes share locks, error limiting info, and cache requests for clients.
From your application you make requests using the task api.


### Starting the Celery Worker
You can start the worker server from either the CLI or your own Python script.
It is recommended to use the CLI unless you plan on registering your own tasks to the celery worker.

#### From CLI

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

#### From your code
You can also start the worker from a Python script if you don't want to set environmental variables.

```python
from EVECelery import EVECeleryWorker

c = EVECeleryWorker(broker_user="user", broker_password="pass", broker_host="host", broker_port=5672,
                    broker_vhost="esi",
                    result_user="user", result_password="pass", result_host="host", result_port=6379, result_db=0)

c.start()
```

### Using the task API from your code
From another Python script you can send tasks to the queues and receive results:

```python
from EVECelery import EVECeleryWorker, TaskDirectory

# only need to make one CeleryWorker in our code to init the tasks and setup connections to RabbitMQ and Redis
# by not passing connection params to CeleryWorker() the connection info will be read from environmental variables
c = EVECeleryWorker()

# note we don't call c.start() here as this is not a worker node script.
# we are calling the task api to submit requests to the message queue which run on the Celery worker nodes

r = TaskDirectory.ESI.Universe.get_universe_regions_region_id.get_sync(region_id=10000053)
# r is the response containing data obtained from ESI
# subsequent calls with the same parameters return results from the cache regardless of requesting client
print(r.dict())
{
  "pydantic_model": "Success200_get_universe_regions_region_id",
  "cache_hit": true,
  "cache_key": "Cache.ESI.Universe.get_universe_regions_region_id.cd252dea2970194b46260124270444f07f4bf449a5fe37ef31f163005fcb50e7",
  "cache_ttl": 31710,
  "headers": {
    "pydantic_model": "SuccessHeaders200_get_universe_regions_region_id",
    "Cache_Control": "public",
    "Content_Language": "en",
    "ETag": null,
    "Expires": "Mon, 17 Apr 2023 11:05:00 GMT",
    "Last_Modified": "Sun, 16 Apr 2023 11:01:07 GMT"
  },
  "constellations": [
    20000609,
    20000610,
    20000611,
    20000612,
    20000613,
    20000614,
    20000615,
    20000616,
    20000617,
    20000618
  ],
  "description": "A natural destination for explorers and adventurers of all kinds, Cobalt Edge ...",
  "name": "Cobalt Edge",
  "region_id": 10000053
}
```

## Copyright Notice

See [CCP.md](https://github.com/NullsecSpace/EVECelery/blob/main/CCP.md)

