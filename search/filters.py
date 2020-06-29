import django_filters
from django_filters import rest_framework as filters
from drf_haystack.filters import HaystackFilter

from search.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price_hr', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price_hr', lookup_expr='lte')
    info = django_filters.CharFilter(field_name='info', method='info_action')

    def info_action(self, queryset, name, value):
        return queryset.extra(where=['CONCAT(title, description) LIKE %s'], params=['%' + value + '%'])

    class Meta:
        model = Advertisement
        fields = ('rooms_count', 'district')


class AdvertisementFilterES(filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price_hr', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price_hr', lookup_expr='lte')

    class Meta:
        model = Advertisement
        fields = ('rooms_count', 'district')
