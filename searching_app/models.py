from django.db import models
from .choices import *

class SaveUrl(models.Model):
    site = models.IntegerField(choices=SITE_CHOICES, default=1)
    url = models.CharField(max_length=1000)


class Seo(models.Model):
    title = models.CharField(max_length=512)
    identifier = models.CharField(max_length=256)
    url = models.CharField(max_length=1024)

    def __unicode__(self):
        return "{} - {}".format(self.identifier, self.title)


class Results(models.Model):
    base_url = models.CharField(default=True, max_length=255)
    url = models.CharField(default=True, max_length=255)
    title = models.CharField(default=True, max_length=255)
    keywords = models.CharField(default=True, max_length=255)
    description = models.CharField(default=True, max_length=255)
    description_unique = models.CharField(default=True, max_length=255)
    title_unique = models.CharField(default=True, max_length=255)
    h1 = models.CharField(default=True, max_length=255)
    h2 = models.CharField(default=True, max_length=255)
    vk = models.CharField(default=True, max_length=255)
    facebook = models.CharField(default=True, max_length=255)
    instagram = models.CharField(default=True, max_length=255)
    broken_link = models.CharField(default=True, max_length=255)
    date_add = models.DateField(auto_now_add=False, blank=True)
    yandex = models.CharField(default=True, max_length=255)
    google = models.CharField(default=True, max_length=255)