from django.db import models


class Map(models.Model):
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)


class Church(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
