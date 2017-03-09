#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-middlewall
------------

Tests for `django-middlewall` middleware module.
"""

from django.test import SimpleTestCase
from django.test import Client
from django.test import override_settings

WHITELIST_MIDDLEWARE_PATH = 'middlewall.middleware.WhitelistMiddleware'
BLACKLIST_MIDDLEWARE_PATH = 'middlewall.middleware.BlacklistMiddleware'


@override_settings(MIDDLEWARE=[WHITELIST_MIDDLEWARE_PATH])
@override_settings(MIDDLEWARE_CLASSES=[WHITELIST_MIDDLEWARE_PATH])
class TestWhitelistMiddlware(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_undefined(self):
        response = self.client.get('/', REMOTE_ADDR='192.0.2.1')
        self.assertEqual(403, response.status_code)

    @override_settings(MIDDLEWALL_WHITELIST=['192.0.2.0/24'])
    def test_hit(self):
        response = self.client.get('/', REMOTE_ADDR='192.0.2.1')
        self.assertEqual(200, response.status_code)

    @override_settings(MIDDLEWALL_WHITELIST=['192.0.2.0/24'])
    def test_miss(self):
        response = self.client.get('/', REMOTE_ADDR='198.51.100.1')
        self.assertEqual(403, response.status_code)


@override_settings(MIDDLEWARE=[BLACKLIST_MIDDLEWARE_PATH])
@override_settings(MIDDLEWARE_CLASSES=[BLACKLIST_MIDDLEWARE_PATH])
class TestBlacklistMiddleware(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_undefined(self):
        response = self.client.get('/', REMOTE_ADDR='192.0.2.1')
        self.assertEqual(200, response.status_code)

    @override_settings(MIDDLEWALL_BLACKLIST=['192.0.2.0/24'])
    def test_hit(self):
        response = self.client.get('/', REMOTE_ADDR='192.0.2.1')
        self.assertEqual(403, response.status_code)

    @override_settings(MIDDLEWALL_BLACKLIST=['192.0.2.0/24'])
    def test_miss(self):
        response = self.client.get('/', REMOTE_ADDR='198.51.100.1')
        self.assertEqual(200, response.status_code)
