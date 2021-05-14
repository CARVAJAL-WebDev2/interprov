from django.conf.urls import url
from OpenTourList import views

urlpatterns = [
	url(r'^$', views.MainPage, name='mainpage'),
	url(r'^OpenTourList/(\d+)/$', views.ViewList, name='viewlist'),
	url(r'^OpenTourList/newlist_url$', views.NewList, name='newlist'),
	url(r'^OpenTourList/(\d+)/addItem$', views.AddItem, name='additem'),	
]

