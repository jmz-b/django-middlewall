# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url
from django.http import HttpResponse


urlpatterns = [
    url(r'^$', lambda r: HttpResponse('', status=200)),
]
