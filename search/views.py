from django.db.models import Min, Max
from django_filters import rest_framework as filters
from drf_haystack.viewsets import HaystackViewSet
from haystack.query import SearchQuerySet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from search.filters import AdvertisementFilter, AdvertisementFilterES
from search.models import Advertisement
from search.serializers import AdvertisementSerializer, AdvertisementHaystackSerializer


class AdvertisementList(generics.ListAPIView):
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        if sort == 'price__asc':
            return Advertisement.objects.all().order_by('price_hr')
        if sort == 'price__desc':
            return Advertisement.objects.all().order_by('-price_hr')
        if sort == 'time__desc':
            return Advertisement.objects.all().order_by('-created')
        if sort == 'time__asc':
            return Advertisement.objects.all().order_by('created')
        return Advertisement.objects.all()


class AdvertisementListES(HaystackViewSet):
    index_models = [Advertisement]
    serializer_class = AdvertisementHaystackSerializer


class Statistics(APIView):
    def get(self, request, format=None):
        return Response({
            'price': {
                'min': Advertisement.objects.all().aggregate(Min('price_hr'))['price_hr__min'],
                'max': Advertisement.objects.all().aggregate(Max('price_hr'))['price_hr__max'],
            },
            'rooms_count': {
                'max': Advertisement.objects.all().aggregate(Max('rooms_count'))['rooms_count__max'],
            }
        })
