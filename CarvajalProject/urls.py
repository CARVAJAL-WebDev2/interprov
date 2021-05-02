from django.conf.urls import url
from OpenTourList import views

urlpatterns = [
	url(r'^$', views.MainPage, name='mainpage'),
	url(r'^OpenTourList/(\d+)/$', views.ViewersList, name='viewerlist'),
	url(r'^OpenTourList/newest_list$', views.NewestList, name='newestlist'),
	url(r'^OpenTourList/(\d+)/addsomeItem$', views.AddSomeItem, name='addsomeitem'),	
]