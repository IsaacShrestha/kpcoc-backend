from django.conf.urls import url, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'hymn', views.HymnViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls)), 
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]