# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hymn(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField(max_length=5000)

	def __unicode__(self):
		return "{0}, {1}".format(self.id, self.title)


