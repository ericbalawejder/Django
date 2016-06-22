from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def index(request):
    #return HttpResponse("The logins index.")
    return render(request, 'index.html')

def by_ip(request):
    #return HttpResponse("The logins index.")
    return render(request, 'by_ip.html')

def by_login(request):
    #return HttpResponse("The logins index.")
    return render(request, 'by_login.html')