from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^rsvp/$', views.rsvp, name='rsvp'),
url(r'^thank-you/$', views.thank_you, name='thank_you'),
]