from django.db import models


class WikiBlob(models.Model):
    wiki_url = models.CharField(primary_key=True, max_length=255)
    wiki_name = models.CharField(max_length=255)
