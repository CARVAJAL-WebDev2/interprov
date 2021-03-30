from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def MainPage(request):
	#return render(request,'mainpage.html')
	return HttpResponse('<html><title> Open Tourist Spots List </title><h1 style="font-color:blue; font-size:22px;" > Here are the Open Tourist Spots with Covid-19 restrictions implemented </h1><input type="text" id="newEntry" name="Entry1" placeholder="Input your desired tourist spot location"><input type="submit" value="Confirm"></html>')