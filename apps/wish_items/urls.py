from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.show_item, name='show_item'),
    url(r'^create$', views.new, name='new'),

]
