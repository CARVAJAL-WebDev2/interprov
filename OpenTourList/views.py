from django.http import HttpResponse
from OpenTourList.models import Item, Recruit
from django.shortcuts import render, redirect

def MainPage(request):
	return render(request, 'mainpage.html')

def ViewList(request, RecId):
	rId = Recruit.objects.get(id=RecId)
	return render(request, 'listpage.html', {'RecId': rId})

def NewList(request):
	newRecruit = Recruit.objects.create()
	Item.objects.create(RecId=newRecruit, text=request.POST['Newmember'])
	return redirect(f'/OpenTourList/{newRecruit.id}/')

def AddItem(request,rId):
	rId = Recruit.objects.get(id=rId)
	Item.objects.create(RecId=rId,text=request.POST['Newmember'])
	return redirect(f'/OpenTourList/{rId.id}/')


	#if request.method == 'POST':
		#Item.objects.create(text=request.POST['Newmember'])
		#return redirect('/Emergency/viewlist_url/')
