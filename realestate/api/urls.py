"""
"""
from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from realestate.api import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r"^", include(router.urls)),
]
