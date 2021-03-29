#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def MainPage(request):
	#return render(request,'mainpage.html')
	return HttpResponse('<html><title>Open Tourist Spots</title><h1 style="color:red; font-size:33px">Open Tourist Spots in the Philippines in observance of CoVid-19 restrictions <br> <input type ="text" id="locationId" name="Entry1" placeholder="Input your preferred tourist location"> <input type="submit" value="Confirm"></html>')