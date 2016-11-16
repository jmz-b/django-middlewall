=================
django-middlewall
=================

Simple middleware for blocking requests by IP Address

Quick start
-----------

1. Add middlewall to INSTALLED_APPS, eg ::

    INSTALLED_APPS = [
        ...
        'middlewall',
    ]


2. Enable middleware components, eg ::

    # enable both white and black listing, prioritize blacklist

    MIDDLEWARE = [
        'middlewall.middleware.BlacklistMiddleware',
        'middlewall.middleware.WhitelistMiddleware',
        ...
    ]

3. Define access lists in CIDR notation, eg ::

    # only allow requests from these subnets

    MIDDLEWALL_WHITELIST = ['192.0.2.0/24', '198.51.100.0/24']

    # also block this specific address

    MIDDLEWALL_BLACKLIST = ['192.0.2.1/32']

4. (optional) Define a custom function to get remote addresses from request
   objects, eg ::

    # take advantage of the X_FORWARDED_FOR support in ipware

    MIDDLEWALL_ADDRESS_GETTER = 'ipware.ip.get_ip'

Refs
----

* ipware_
.. _ipware: https://github.com/un33k/django-ipware
