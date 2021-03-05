from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^pictures/$', views.pictures, name='pictures'),
]