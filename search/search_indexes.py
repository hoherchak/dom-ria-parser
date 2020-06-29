from haystack import indexes
from search.models import Advertisement


class AdvertisementIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True, template_name='search/ad_index.txt')
    code = indexes.IntegerField(model_attr='code')
    title = indexes.CharField(model_attr='title')
    short_title = indexes.CharField(model_attr='short_title')
    description = indexes.CharField(model_attr='description')
    district = indexes.CharField(model_attr='district')
    rooms_count = indexes.IntegerField(model_attr='rooms_count')
    url = indexes.CharField(model_attr='url')
    image = indexes.CharField(model_attr='image')
    price_hr = indexes.IntegerField(model_attr='price_hr')
    price_usd = indexes.IntegerField(model_attr='price_usd')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Advertisement
