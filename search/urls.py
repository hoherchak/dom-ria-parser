from django.conf.urls import url
from rest_framework import routers

from search.views import AdvertisementList, Statistics, AdvertisementListES
router = routers.DefaultRouter()
router.register('ads_es', AdvertisementListES, base_name='ads_es')

urlpatterns = [
    url(r'^ads/', AdvertisementList.as_view(), name='ads'),
    url(r'^stats/', Statistics.as_view(), name='stats')

] + router.urls
