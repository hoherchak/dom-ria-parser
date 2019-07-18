from rest_framework import generics

from search.models import Advertisement
from search.serializers import AdvertisementSerializer


class AdvertisementList(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
