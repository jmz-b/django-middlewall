=====
Usage
=====

To use Django Middlewall in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'middlewall.apps.MiddlewallConfig',
        ...
    )

Add Django Middlewall's URL patterns:

.. code-block:: python

    from middlewall import urls as middlewall_urls


    urlpatterns = [
        ...
        url(r'^', include(middlewall_urls)),
        ...
    ]
