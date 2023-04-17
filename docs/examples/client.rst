Client
======

Client code from other applications requires connectivity to RabbitMQ and and Redis along with running worker nodes.

When making calls to tasks always ensure you use the task object's ``get_sync()`` function or through the various methods documented `here <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_.

Calling the task body directly through the task's ``run()`` method executes the task in the context of the client instead of a Celery worker node.


Get a character's public info
-----------------------------
This sample returns character information from ESI using a synchronous call.

.. code:: python

    from EVECelery import EVECeleryWorker, TaskDirectory

    c = EVECeleryWorker()

    r = TaskDirectory.ESI.Character.get_characters_character_id.get_sync(character_id=2118421377)
    print(r.dict())

Prints a response:

.. code:: json

    {
      "pydantic_model": "Success200_get_characters_character_id",
      "cache_hit": true,
      "cache_key": "Cache.ESI.Character.get_characters_character_id.9c7cfb14c597cb21252063c7a3fc9c91d8c25c2074055c040ffc74e7c4f28d31",
      "cache_ttl": 642,
      "headers": {
        "pydantic_model": "SuccessHeaders200_get_characters_character_id",
        "Cache_Control": "public",
        "ETag": null,
        "Expires": "Mon, 17 Apr 2023 05:17:36 GMT",
        "Last_Modified": "Sun, 16 Apr 2023 05:17:36 GMT"
      },
      "alliance_id": 434243723,
      "birthday": "2021-03-11T14:06:59Z",
      "bloodline_id": 7,
      "corporation_id": 109299958,
      "description": "<font size=\"13\" color=\"#ffbfbfbf\"></font><font size=\"13\" color=\"#ffffffff\">Community ...",
      "faction_id": null,
      "gender": "male",
      "name": "CCP Swift",
      "race_id": 8,
      "security_status": 1.4928743770000001,
      "title": null
    }

.. note::
    By using the ``get_sync()`` call this code will block until the task returns the result or the timeout occurs.

    If you require asynchronous invocation see `Celery calling tasks guide <https://docs.celeryq.dev/en/stable/userguide/calling.html>`_ to return a async result / promise that you later retrieve the result from.

Get route distance between two solar systems
--------------------------------------------
In this sample obtain a list of system ids between the origin and destination systems.

.. code:: python

    from EVECelery import EVECeleryWorker, TaskDirectory

    c = EVECeleryWorker()

    r = TaskDirectory.ESI.Routes.get_route_origin_destination.get_sync(origin=30000142, destination=30002659)
    print(r.dict())

Prints the response:

.. code:: json

    {
      "pydantic_model": "Success200_get_route_origin_destination",
      "cache_hit": false,
      "cache_key": "Cache.ESI.Routes.get_route_origin_destination.41eee8e6e9b8d0236c6776cf0b683effaf2f40cdcf07e9329557c33826f62295",
      "cache_ttl": 4264,
      "headers": {
        "pydantic_model": "SuccessHeaders200_get_route_origin_destination",
        "Cache_Control": "public",
        "ETag": null,
        "Expires": "Mon, 17 Apr 2023 06:21:48 GMT",
        "Last_Modified": "Sun, 16 Apr 2023 06:21:48 GMT"
      },
      "items": [
        30000142,
        30000138,
        30001379,
        30001376,
        30002813,
        30002809,
        30002811,
        30002812,
        30005334,
        30005331,
        30005203,
        30002661,
        30002659
      ]
    }

.. note::
    All ESI results are typically cached so subsequent calls using the same parameters will read from the cache instead of making new ESI calls.

Get alliance info
---------------------
Return system information for a given solar system ID.

.. code:: python

    from EVECelery import EVECeleryWorker

    c = EVECeleryWorker()

    TaskDirectory.ESI.Alliance.get_alliances_alliance_id.get_sync(alliance_id=1727758877)
    print(r.dict())

Returns the response:

.. code:: json

    {
      "pydantic_model": "Success200_get_alliances_alliance_id",
      "cache_hit": true,
      "cache_key": "Cache.ESI.Alliance.get_alliances_alliance_id.b8aae887a4ea7c973bc4e130f0a6f6cc94b733a639f74591aee9787ee172f1e3",
      "cache_ttl": 226,
      "headers": {
        "pydantic_model": "SuccessHeaders200_get_alliances_alliance_id",
        "Cache_Control": "public",
        "ETag": null,
        "Expires": "Mon, 17 Apr 2023 05:18:45 GMT",
        "Last_Modified": "Mon, 17 Apr 2023 04:18:45 GMT"
      },
      "creator_corporation_id": 1727573569,
      "creator_id": 1395811708,
      "date_founded": "2010-08-12T00:46:00Z",
      "executor_corporation_id": 1727573569,
      "faction_id": null,
      "name": "Northern Coalition.",
      "ticker": "NC"
    }

