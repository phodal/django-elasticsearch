# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import re
from django.contrib import admin

from django.contrib.gis.geos import Point
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.db import models
from pygeocoder import Geocoder


class Note(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
        # help_text=_('Required. 30 characters or fewer. Letters, numbers and '
        #             '@/./+/-/_ characters'),
        # validators=[
        #     validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        # ])
    email = models.EmailField("邮箱", blank=True)
    phone_number = models.CharField("手机号", max_length=11, unique=True,
        validators=[
            validators.RegexValidator(re.compile('^\+?1?\d{9,15}$'), _('Enter a valid Phone Number.'), 'invalid')
        ])
    number = models.IntegerField("数量", max_length=10)
    price = models.FloatField("价格", max_length=5)
    title = models.CharField("标题", max_length=1000)
    body = models.TextField("简介")
    province = models.CharField("省", max_length=10)
    city = models.CharField("市", max_length=10)
    address = models.CharField("地址", max_length=10)
    timestamp = models.DateTimeField(auto_now=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        #Geocode the address
        results = Geocoder.geocode(self.province + self.city + self.address)
        self.latitude = results[0].coordinates[0]
        self.longitude = results[0].coordinates[1]
        super(Note, self).save(*args, **kwargs)

    def get_location(self):
        return Point(self.longitude, self.latitude)

    def get_location_info(self):
        return self.province + self.city + self.address

admin.site.register(Note)