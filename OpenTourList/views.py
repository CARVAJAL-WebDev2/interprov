from django.shortcuts import render, redirect
from OpenTourList.models import Item
from django.http import HttpResponse

def MainPage(request):
	return render(request,'mainpage.html')
	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['idName'])
	# 	return redirect('/OpenTourList/listview_url/')
	#return render(request,'mainpage.html',)
	#items = Item.objects.all()
	# , {'newTouristName': items}

def ListView(request):
	items = Item.objects.all()
	return render(request,'listview.html',{'newTouristName': items})

def ListNew(request):
	Item.objects.create(text=request.POST['idName'])
	return redirect('/OpenTourList/listview_url/')

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