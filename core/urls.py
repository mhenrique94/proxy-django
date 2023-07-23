from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_proxies, name="index"),
]