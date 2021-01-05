from django.shortcuts import render

# Create your views here.
def nav(request):
	return render(request,'studentproject/nav.html')