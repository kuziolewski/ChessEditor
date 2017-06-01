from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^turniej/(?P<pk>\d+)/$', views.turniej, name='turniej'),
    url(r'^rozgrywka/(?P<pk>\d+)/$', views.rozgrywka, name='rozgrywka'),
]

