from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse

list_of_name = ['raju','chutki','jaggu','', 'kaliya']
# Create your views here.
def func_name1(request,count):
    if list_of_name[count]:
        redirect_path=reverse("naming_url",args=[list_of_name[count]])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponse("name not in give index")
    
def func_name2(request,name):
    if(name):
        return HttpResponse(name)
    else:
        return HttpResponse("Name not Found in given index")    
    