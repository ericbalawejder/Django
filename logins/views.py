from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from logins.models import Fail
 
def index(request):
    #fail = Fail.objects.filter(visible=True)
    failed = Fail.objects.all()
    print failed
    context = {'failed': failed}
    return render(request, 'index.html', context)

def by_ip(request):
    #return HttpResponse("The logins index.")
    failed = Fail.objects.all().distinct()
    for item in failed:
        print item
        context = {'failed': failed}
        return render(request, 'by_ip.html', context)

def by_login(request):
    #return HttpResponse("The logins index.")
    failed = Fail.objects.all().distinct()
    for item in failed:
        print item
        context = {'failed': failed}
        return render(request, 'by_login.html', context)

from django.shortcuts import get_object_or_404
 
def details(request, fail_id):
    fail = get_object_or_404(Fail, pk = fail_id)
    return render(request, 'details.html', {'fail': fail})


