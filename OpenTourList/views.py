from django.shortcuts import render
#from django.http import HttpResponse

def MainPage(request):
	return render(request,'mainpage.html',{'newTouristName': request.POST.get('idName'),'newSwabCode': request.POST.get('idUniCode'),'newDestination': request.POST.get('idLocEntry',''),})

#MainPage = None
	#pass
	#return HttpResponse('<html><title> CoVid-19 Enhanced Local Travel Registration </title></html>')