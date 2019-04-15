from django.shortcuts import render

from django.http import HttpResponse

app_name = 'main'


def homepage(request):
	return render(request,'main/home.html')
	#return HttpResponse("hiiii himani")
# Create your views here.
