# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
from django.contrib import admin

from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

admin.site.register(Note)