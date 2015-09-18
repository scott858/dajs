from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.example_app_view, name='main'),
    url(r'^plot/$', views.plot_view, name='plot'),
)
