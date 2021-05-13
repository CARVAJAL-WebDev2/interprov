from django.conf.urls import url
from OpenTourList import views

urlpatterns = [
	url(r'^$', views.MainPage, name='mainpage'),
	url(r'^Emergency/(\d+)/$', views.ViewList, name='viewlist'),
	url(r'^Emergency/newlist_url$', views.NewList, name='newlist'),
	url(r'^Emergency/(\d+)/addItem$', views.AddItem, name='additem'),	
]
