from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.FloatField()
    amount = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )
    vendor = models.ForeignKey(
        'Vendor',
        on_delete=models.SET_NULL,
        null=True,
    )
    tag = models.ManyToManyField(
        'Tag',
    )

    def __unicode__(self):
        return 'Item ' + self.title

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return 'Category ' + self.title

class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return 'Tag ' + self.title

class Vendor(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return 'Vendor ' + self.title
