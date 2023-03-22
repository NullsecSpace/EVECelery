Welcome to EVECelery's documentation!
=====================================

EVECelery is a distributed task queue framework for building tools that interact with the EVE Online `ESI`_ using Celery, RabbitMQ, and Redis.

With EVECelery you can easily distribute ESI calls across task queues built on top of `Celery`_ with a fleet of worker nodes.
You can build on top of EVECelery to create your own tools defining custom tasks and scheduled jobs.


.. _ESI: https://esi.evetech.net/ui
.. _Celery: https://docs.celeryq.dev/

User Guide
==========
User guide for using the library.

.. toctree::
    :maxdepth: 3

    user_guide/index

Examples
========
Code samples of this library.

.. toctree::
    :maxdepth: 3

    examples/index

Contributor Guide
=================
Resources for further developing this library and making contributions.

.. toctree::
    :maxdepth: 3

    contributor_guide/index

API Reference
=============

.. toctree::
    :maxdepth: 3

    API Reference <autoapi/EVECelery/index>




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
