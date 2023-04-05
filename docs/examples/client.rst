Client
======

Client code from other applications requires connectivity to RabbitMQ and and Redis along with running worker nodes.

Get a character's public info
-----------------------------
This sample imports the Character API tasks that returns character information from ESI using a synchronous call.

.. code:: python

    from EVECelery import EVECeleryWorker
    from EVECelery.tasks.Character import *

    c = EVECeleryWorker()

    r = CharacterPublicInfo().get_sync(timeout=5, character_id=1326083433)
    print(r)


.. note::
    By using the ``get_sync()`` call this code will block until the task returns the result or the timeout occurs.

    If you require asynchronous invocation use the ``get_async`` method to return a async result / promise that you later retrieve the result from.

Get route distance between two solar systems
--------------------------------------------
In this sample we use the obtain a list of system ids between the origin and destination systems.

.. code:: python

    from EVECelery import EVECeleryWorker
    from EVECelery.tasks.Routes import *

    c = EVECeleryWorker()

    r = Route().get_sync(timeout=5, origin=30000142, destination=30002659)  # Jita to Dodixie - 12 jumps
    print(f"Jumps: {len(r) - 1} Systems: {r} ")

.. note::
    All ESI results are typically cached so subsequent calls using the same parameters will read from the cache instead of making new ESI calls.

Get solar system info
---------------------
Return system information for a given solar system ID.

.. code:: python

    from EVECelery import EVECeleryWorker
    from EVECelery.tasks.Universe import *

    c = EVECeleryWorker()
    r = SystemInfo().get_sync(timeout=5, system_id=30000142)
    print(r)

