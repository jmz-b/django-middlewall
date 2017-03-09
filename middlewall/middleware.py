# -*- coding: utf-8 -*-
from netaddr import IPAddress, IPSet

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.utils.module_loading import import_string

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

DEFAULT_GETTER = 'middlewall.utils.get_remote_addr'


def get_ipaddr(request):
    path = getattr(settings, 'MIDDLEWALL_ADDRESS_GETTER', DEFAULT_GETTER)
    func = import_string(path)
    return IPAddress(func(request))


def get_ipset_from_settings(name):
    return IPSet(getattr(settings, name, []))


class WhitelistMiddleware(MiddlewareMixin):
    def process_request(self, request):
        whitelist = get_ipset_from_settings('MIDDLEWALL_WHITELIST')
        if not get_ipaddr(request) in whitelist:
            raise PermissionDenied


class BlacklistMiddleware(MiddlewareMixin):
    def process_request(self, request):
        blacklist = get_ipset_from_settings('MIDDLEWALL_BLACKLIST')
        if get_ipaddr(request) in blacklist:
            raise PermissionDenied
