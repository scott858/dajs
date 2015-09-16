from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.admin_view, name='admin'),
    url(r'^admin$', views.admin_view, name='admin'),
    url(r'^main$', views.main_view, name='main'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^products$', views.products_view, name='products'),
    url(r'^orders$', views.orders_view, name='orders'),
)
