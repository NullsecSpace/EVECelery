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
    print(json.dumps(r.dict(), indent=2, default=str))

Prints a response:

.. code:: json

    {
      "pydantic_model": "Response200_get_characters_character_id",
      "cache": {
        "hit": false,
        "key": "Cache.ESI.Character.get_characters_character_id.9c7cfb14c597cb21252063c7a3fc9c91d8c25c2074055c040ffc74e7c4f28d31",
        "ttl": 69357
      },
      "headers": {
        "Cache_Control": "public",
        "ETag": null,
        "Expires": "Mon, 24 Apr 2023 04:06:50 GMT",
        "Last_Modified": "Sun, 23 Apr 2023 04:06:50 GMT"
      },
      "body": {
        "alliance_id": 434243723,
        "birthday": "2021-03-11 14:06:59+00:00",
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
    print(json.dumps(r.dict(), indent=2, default=str))

Prints the response:

.. code:: json

    {
      "pydantic_model": "Response200_get_route_origin_destination",
      "cache": {
        "hit": false,
        "key": "Cache.ESI.Routes.get_route_origin_destination.41eee8e6e9b8d0236c6776cf0b683effaf2f40cdcf07e9329557c33826f62295",
        "ttl": 24581
      },
      "headers": {
        "Cache_Control": "public",
        "ETag": null,
        "Expires": "Sun, 23 Apr 2023 15:39:28 GMT",
        "Last_Modified": "Sat, 22 Apr 2023 15:39:28 GMT"
      },
      "body": [
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
Return alliance information for a given alliance id.

.. code:: python

    from EVECelery import EVECeleryWorker, TaskDirectory

    c = EVECeleryWorker()

    r = TaskDirectory.ESI.Alliance.get_alliances_alliance_id.get_sync(alliance_id=1727758877)
    print(json.dumps(r.dict(), indent=2, default=str))

Returns the response:

.. code:: json

    {
      "pydantic_model": "Response200_get_alliances_alliance_id",
      "cache": {
        "hit": true,
        "key": "Cache.ESI.Alliance.get_alliances_alliance_id.b8aae887a4ea7c973bc4e130f0a6f6cc94b733a639f74591aee9787ee172f1e3",
        "ttl": 3175
      },
      "headers": {
        "Cache_Control": "public",
        "ETag": null,
        "Expires": "Sun, 23 Apr 2023 09:41:23 GMT",
        "Last_Modified": "Sun, 23 Apr 2023 08:41:23 GMT"
      },
      "body": {
        "creator_corporation_id": 1727573569,
        "creator_id": 1395811708,
        "date_founded": "2010-08-12 00:46:00+00:00",
        "executor_corporation_id": 1727573569,
        "faction_id": null,
        "name": "Northern Coalition.",
        "ticker": "NC"
      }
    }

Get system info
---------------------
Return system info for a given system ID.

.. code:: python

    from EVECelery import EVECeleryWorker, TaskDirectory

    c = EVECeleryWorker()

    r = TaskDirectory.ESI.Universe.get_universe_systems_system_id.get_sync(system_id=30000142)
    print(json.dumps(r.dict(), indent=2, default=str))

Returns the response:

.. code:: json

    {
      "pydantic_model": "Response200_get_universe_systems_system_id",
      "cache": {
        "hit": false,
        "key": "Cache.ESI.Universe.get_universe_systems_system_id.baeb293ec43003bd8a2b14cbaa947a3cefd0a95b812a27be0a9e700b0804d6ca",
        "ttl": 7875
      },
      "headers": {
        "Cache_Control": "public",
        "Content_Language": "en",
        "ETag": null,
        "Expires": "Sun, 23 Apr 2023 11:05:00 GMT",
        "Last_Modified": "Sat, 22 Apr 2023 11:01:05 GMT"
      },
      "body": {
        "constellation_id": 20000020,
        "name": "Jita",
        "planets": [
          {
            "asteroid_belts": null,
            "moons": null,
            "planet_id": 40009077
          },
          {
            "asteroid_belts": null,
            "moons": null,
            "planet_id": 40009078
          },
          {
            "asteroid_belts": null,
            "moons": [
              40009081
            ],
            "planet_id": 40009080
          },
          {
            "asteroid_belts": null,
            "moons": [
              40009083,
              40009084,
              40009085,
              40009087,
              40009088,
              40009089,
              40009090,
              40009091,
              40009092,
              40009093,
              40009094,
              40009097
            ],
            "planet_id": 40009082
          },
          {
            "asteroid_belts": null,
            "moons": [
              40009099,
              40009100,
              40009101,
              40009102,
              40009103,
              40009104,
              40009105,
              40009106,
              40009107,
              40009108,
              40009109,
              40009110,
              40009111,
              40009112,
              40009113,
              40009114,
              40009115
            ],
            "planet_id": 40009098
          },
          {
            "asteroid_belts": null,
            "moons": [
              40009118
            ],
            "planet_id": 40009116
          },
          {
            "asteroid_belts": null,
            "moons": [
              40009121,
              40009122
            ],
            "planet_id": 40009119
          },
          {
            "asteroid_belts": null,
            "moons": null,
            "planet_id": 40009123
          }
        ],
        "position": {
          "x": -1.29064861735e+17,
          "y": 6.075530691e+16,
          "z": 1.1746922706e+17
        },
        "security_class": "B",
        "security_status": 0.9459131360054016,
        "star_id": 40009076,
        "stargates": [
          50001248,
          50001249,
          50001250,
          50013876,
          50013913,
          50013921,
          50013928
        ],
        "stations": [
          60000361,
          60000364,
          60000451,
          60000463,
          60002953,
          60002959,
          60003055,
          60003460,
          60003463,
          60003466,
          60003469,
          60003757,
          60003760,
          60004423,
          60015169
        ],
        "system_id": 30000142
      }
    }

