from django_filters import rest_framework as filters
from rest_framework import generics

from search.filters import AdvertisementFilter
from search.models import Advertisement
from search.serializers import AdvertisementSerializer


class AdvertisementList(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter
