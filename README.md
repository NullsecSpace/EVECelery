# ESIRabbit
ESI API requests library using [RabbitMQ](https://www.rabbitmq.com/), [celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html) tasks queues, and [Redis](https://redis.io/) caching.

# Installation
```
pip install git+https://github.com/EVEInsight/ESIRabbit.git
```

# Usage
From your worker code start the Celery worker server that handles running tasks:
```python
from ESIRabbit import CeleryApp

c = CeleryApp(broker_user="user", broker_password="pass", broker_host="host", broker_port=5672, broker_vhost="esi",
              result_user="user", result_password="pass", result_host="host", result_port=6379, result_db=0,
              header_email="youremail@example.com")

c.start() # Start celery app - equivalent to running "celery worker -l WARNING --autoscale 10,1 -Q queues"
```

From another Python script you can send tasks to the queues and receive results:
```python
from ESIRabbit import CeleryApp
from ESIRabbit.tasks.Universe import *

c = CeleryApp(broker_user="user", broker_password="pass", broker_host="host", broker_port=5672, broker_vhost="esi",
              result_user="user", result_password="pass", result_host="host", result_port=6379, result_db=0,
              header_email="youremail@example.com") # only need to call this once in our code to init the tasks
r = SystemInfo().get_sync(timeout=5, system_id=30000142)
print(r)
```

# Current supported endpoints

| ESI Route                                    | ESIRabbit Task        |
|----------------------------------------------|-----------------------|
| /alliances/{alliance_id}/                    | AllianceInfo()        |
| /characters/{character_id}/                  | CharacterPublicInfo() |
| /corporations/{corporation_id}/              | CorporationInfo()     |
| /markets/prices/                             | PricesList()          |
| /universe/categories/{category_id}/          | CategoryInfo()        |
| /universe/constellations/{constellation_id}/ | ConstellationInfo()   |
| /universe/factions/                          | FactionsList()        |
| /universe/groups/{group_id}/                 | GroupInfo()           |
| /universe/regions/{region_id}/               | RegionInfo()          |
| /universe/systems/{system_id}/               | SystemInfo()          |
| /universe/types/{type_id}/                   | TypeInfo()            |

# Examples
See the included example scripts under [docs/examples](https://github.com/EVEInsight/ESIRabbit/tree/main/docs/examples)

# Copyright Notice
See CCP.md

