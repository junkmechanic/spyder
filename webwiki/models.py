from django.db import models


class WikiBlob(models.Model):
    url = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    links = models.TextField()
    weighed_links = models.ForeignKey('WeighedLinks')
    word_dict = models.ForeignKey('WordDict')


class WeighedLinks(models.Model):
    key = models.CharField(max_length=100)
    value = models.FloatField()


class WordDict(models.Model):
    key = models.CharField(max_length=100)
    value = models.FloatField()
