Welcome to EVECelery's documentation!
=====================================

EVECelery is a distributed task queue framework for building tools that interact with
the `EVE Online ESI API <https://esi.evetech.net/ui>`_ using Celery, RabbitMQ, and Redis.

With EVECelery you can easily distribute ESI calls and tasks across a fleet of worker nodes built using `Celery <https://docs.celeryq.dev/>`_.

You can create your own tasks on top of EVECelery defining custom functions and scheduled jobs that run alongside the included tasks.

Features
==========
* Built with `Celery <https://docs.celeryq.dev/>`_ to distribute ESI calls and tasks across a fleet of worker nodes

* Distributed locking system with Redis ensures stateless workers won't make duplicate API calls if multiple clients run tasks with matching parameters at the same time

* Cache integration with Redis that caches ESI responses

* Easily define your own Celery tasks to register with the EVECelery worker nodes

* Client support for obtaining results synchronously or asynchronously. See `Celery calling tasks <https://docs.celeryq.dev/>`_ for docs on calling tasks.

* Automated task retry and distributed error rate control limiting across the worker fleet

* ESI task API designed to mirror the `ESI Swagger Spec <https://esi.evetech.net/ui/>`_ with the same parameter names, responses, and documentation for easy development and code completion

* Support for periodic scheduled tasks making use of the `Celery beat scheduler <https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html>`_


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
