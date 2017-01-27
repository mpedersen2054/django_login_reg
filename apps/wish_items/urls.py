from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.show_item, name='show_item'),
    url(r'^create$', views.new, name='new'),
    url(r'^create_item$', views.create, name='create'),
    url(r'^remove/(?P<id>\d+)$', views.remove_item, name='remove_item'),
    url(r'^delete/(?P<id>\d+)$', views.delete_item, name='delete_item'),
    url(r'^add_item/(?P<id>\d+)$', views.add_item, name='add_item'),

]
