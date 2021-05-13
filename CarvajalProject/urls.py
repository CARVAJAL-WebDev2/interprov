from django.conf.urls import url
from OpenTourList import views

urlpatterns = [
	url(r'^$', views.MainPage, name='mainpage'),
	url(r'^OpenTourList/(\d+)/$', views.ViewersList, name='viewerslist'),
	url(r'^OpenTourList/newestlist$', views.NewestList, name='newestlist'),
	url(r'^OpenTourList/(\d+)/addItem$', views.AddSomeItem, name='addsomeitem'),	
]

