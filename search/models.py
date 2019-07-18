from django.db import models


class Advertisement(models.Model):
    code = models.IntegerField()
    title = models.TextField()
    short_title = models.TextField()
    description = models.TextField(null=True, blank=True)
    district = models.TextField(null=True, blank=True)
    rooms_count = models.IntegerField()
    url = models.TextField()
    image = models.TextField(null=True, blank=True)
    price_hr = models.IntegerField()
    price_usd = models.IntegerField()
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def info(self):
        return self.title + ' ' + self.description
