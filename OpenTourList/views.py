from django.http import HttpResponse
from OpenTourList.models import Item, Tourist
from django.shortcuts import render, redirect

def MainPage(request):
	return render(request, 'mainpage.html')

def ViewersList(request, RecId):
	tId = Tourist.objects.get(id=TourId)
	return render(request, 'listpage.html', {'tId': tId})

def NewestList(request):
	newTourist = Tourist.objects.create()
	Item.objects.create(TourId=newTourist, text=request.POST['idName'])
	return redirect(f'/OpenTourList/{newTourist.id}/')

def AddSomeItem(request,rId):
	tId = Tourist.objects.get(id=tId)
	Item.objects.create(TourId=tId,text=request.POST['idName'])
	return redirect(f'/OpenTourList/{tId.id}/')

# 	pass

	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['idName'])
		# return redirect('/OpenTourList/listview_link/')
	# return redirect('mainpage.html')
	# items = Item.objects.all()
	 #, {'newTouristName': items})
	#if request.method == 'POST':
	#	item1 = request.POST['idName']
	#	Item.objects.create(text=request.POST['idName'])
	#	return redirect('/')
	#else:
	#	item1 = ''
	#return render(request,'mainpage.html', {'newTouristName': item1,})

	#item1 = Item() 
	#item1.text=request.POST.get('idName','')
	#item1.save()
	#return render(request,'mainpage.html',{'newTouristName': item1.text,})

#return render(request,'mainpage.html',{'newTouristName': request.POST.get('idName'),'newSwabCode': request.POST.get('idUniCode'),'newDestination': request.POST.get('idLocEntry',''),})
#MainPage = None
	#pass
	#return HttpResponse('<html><title> CoVid-19 Enhanced Local Travel Registration </title></html>')
