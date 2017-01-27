from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register_user$', views.register, name='register_user'),
    url(r'^login_user$', views.login, name='login_user'),
    url(r'^success$', views.success, name='success'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),
]
