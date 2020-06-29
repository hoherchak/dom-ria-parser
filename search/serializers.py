from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers

from search.models import Advertisement
from search.search_indexes import AdvertisementIndex


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        exclude = []


class AdvertisementHaystackSerializer(HaystackSerializer):
    class Meta:
        index_classes = [AdvertisementIndex]
        exclude = []
