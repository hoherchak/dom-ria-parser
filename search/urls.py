from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from search.views import AdvertisementList, Statistics

urlpatterns = [
    url(r'^ads/', AdvertisementList.as_view(), name='ads'),
    url(r'^stats/', Statistics.as_view(), name='stats'),
]