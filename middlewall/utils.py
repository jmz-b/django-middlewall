# -*- coding: utf-8 -*-

def get_remote_addr(request):
    return request.META['REMOTE_ADDR']
