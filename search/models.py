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
        return self.title

    def info(self):
        return self.title + ' ' + self.description
