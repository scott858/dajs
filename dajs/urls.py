from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from api.views import ToDoViewset, ProductViewset, OrderViewset

router = routers.DefaultRouter()
router.register(r'todo', ToDoViewset)
router.register(r'products', ProductViewset)
router.register(r'orders', OrderViewset)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls, namespace='api_v1')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^todo/', include('todo.urls', namespace='todo')),
    url(r'^sports-store/', include('sports_store.urls', namespace='sports_store')),
    url(r'^', include('chatserver.urls', namespace='chat')),
)
