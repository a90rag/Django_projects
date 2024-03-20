from django.shortcuts import render
from django.http import HttpResponse

def january(request):
    return HttpResponse("it's january")
def februry(request):
    return HttpResponse("it's fabrury")
    
def month_name(request,month):
    if month=='march':
        ret="it's march"
    elif month=='appril':
        ret="it's april fool"
    else:
        ret="spacify starting 4 months"
    return HttpResponse(ret)            
# Create your views here.
