from django.http import HttpResponse
from OpenTourList.models import Item, Tourist
from django.shortcuts import render, redirect

def MainPage(request):
	return render(request, 'mainpage.html')

def ViewList(request, TourId):
	tId = Tourist.objects.get(id=TourId)
	return render(request, 'listpage.html', {'TourId': tId})

def NewList(request):
	newTourist = Tourist.objects.create()
	Item.objects.create(TourId=newTourist, text=request.POST['idName'])
	return redirect(f'/OpenTourList/{newTourist.id}/')

def AddItem(request,tId):
	tId = Tourist.objects.get(id=tId)
	Item.objects.create(TourId=tId,text=request.POST['idName'])
	return redirect(f'/OpenTourList/{tId.id}/')


	#if request.method == 'POST':
		#Item.objects.create(text=request.POST['Newmember'])
		#return redirect('/Emergency/viewlist_url/')
