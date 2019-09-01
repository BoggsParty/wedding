from django.conf.urls import include, url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^$', views.main, name='home'),
url(r'^totals/', views.totals, name='totals'),
path('accounts/', include('django.contrib.auth.urls')),
]