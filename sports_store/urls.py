from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^', views.sports_store_view, name='home'),
)
