from django.conf.urls import url
from django.http import HttpResponse


urlpatterns = [
    url(r'^$', lambda r: HttpResponse('', status=200)),
]
