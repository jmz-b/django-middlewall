=============================
Django Middlewall
=============================

.. image:: https://badge.fury.io/py/django-middlewall.svg
    :target: https://badge.fury.io/py/django-middlewall

.. image:: https://travis-ci.org/jmz-b/django-middlewall.svg?branch=master
    :target: https://travis-ci.org/jmz-b/django-middlewall

.. image:: https://codecov.io/gh/jms-b/django-middlewall/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jmz-b/django-middlewall

Simple middleware for blocking requests by IP Address


Quickstart
----------

Install Django Middlewall::

    pip install django-middlewall

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'middlewall.apps.MiddlewallConfig',
        ...
    )

Enable middleware components:

.. code-block:: python

    # enable both white and black listing

    MIDDLEWARE = [
        'middlewall.middleware.BlacklistMiddleware',
        'middlewall.middleware.WhitelistMiddleware',
        ...
    ]

Define access lists in CIDR notation:

.. code-block:: python

    # only allow requests from these subnets

    MIDDLEWALL_WHITELIST = ['192.0.2.0/24', '198.51.100.0/24']

    # also block this specific address

    MIDDLEWALL_BLACKLIST = ['192.0.2.1/32']

(optional) Define a custom function to get remote addresses from request
objects:

.. code-block:: python

    # take advantage of the X_FORWARDED_FOR support in ipware

    MIDDLEWALL_ADDRESS_GETTER = 'ipware.ip.get_ip'


Running Tests
-------------

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -e .[test]
    (myenv) $ pip install tox
    (myenv) $ tox


Credits
-------

*  Cookiecutter_
*  `cookiecutter-djangopackage`_
*  ipware_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _ipware: https://github.com/un33k/django-ipware
