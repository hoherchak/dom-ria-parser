from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from search.views import AdvertisementList

urlpatterns = [
    url(r'^ads/', AdvertisementList.as_view(), name='ads'),
]