from django.db import models


class Advertisement(models.Model):
    title = models.TextField()
    short_title = models.TextField()
    description = models.TextField()
    district = models.TextField()
    rooms_count = models.IntegerField()
    price_hr = models.IntegerField()
    price_usd = models.IntegerField()


    def __str__(self):
        return '{} ({}, {} rooms, {} hrn - {} usd, {})'.format(self.title, self.district, self.rooms_count, self.price_hr, self.price_usd, self.description)
