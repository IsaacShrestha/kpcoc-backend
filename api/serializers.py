from rest_framework import serializers
from .models import *


class HymnSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Hymn
		fields = ('id', 'title', 'body')