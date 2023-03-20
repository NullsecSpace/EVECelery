Welcome to EVECelery's documentation!
=====================================

EVECelery is a distributed task queue framework for building tools that interact with the EVE Online `ESI`_ using Celery, RabbitMQ, and Redis.

With EVECelery you can easily distribute ESI calls across task queues built on top of `Celery`_ with a fleet of worker nodes.
You can build on top of EVECelery to create your own tools defining custom tasks and scheduled jobs.


.. _ESI: https://esi.evetech.net/ui
.. _Celery: https://docs.celeryq.dev/


.. toctree::
    :caption: Package Documentation
    :maxdepth: 4
    :numbered:

    usage/installation
    usage/quickstart


.. toctree::
    :caption: Examples and Code Samples
    :maxdepth: 4

    examples/worker
    examples/client


.. toctree::
    :caption: API Reference
    :name: autoapi_evecelery
    :maxdepth: 3

    autoapi/EVECelery/index

.. toctree::
    :caption: Project Links
    :maxdepth: 3
    :hidden:

    GitHub <https://github.com/NullsecSpace/EVECelery>
    Issues <https://github.com/NullsecSpace/EVECelery/issues>
    Docs <https://evecelery.nullsec.space/>
    PyPI <https://pypi.org/project/EVECelery/>




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
