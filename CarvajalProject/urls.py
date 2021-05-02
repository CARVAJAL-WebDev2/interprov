from django.conf.urls import url
from OpenTourList import views

urlpatterns = [
	url(r'^$', views.MainPage, name='mainpage'),
	url(r'^OpenTourList/listnew_link$', views.ListNew, name='listnew'),
	url(r'^OpenTourList/(\d+)/$', views.ListView, name='listview'),
	url(r'^OpenTourList/(\d+)/itemAdd$', views.ItemAdd, name='itemadd'),
 ]