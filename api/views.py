# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from serializers import *
from .models import *

# Create your views here.

# Hymn viewset
class HymnViewSet(viewsets.ModelViewSet):
	queryset = Hymn.objects.all()
	serializer_class = HymnSerializer


