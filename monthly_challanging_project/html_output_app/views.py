from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

def func_name1(request,value):
    if value%2==0:
        path_redirect=reverse("name2",args=[value])
    elif value%2 !=0:
        path_redirect=reverse("name2",args=["odd"])
    else:
        #return HttpResponseRedirect(reverse('name2',args=[f"<h3>please enter any no.<\h3>"]))
        return HttpResponse(f"<h3>please enter any no.<\h3>")    
    return HttpResponseRedirect(path_redirect)

def func_name2(request,value):
    return HttpResponse(f"<ul><li>this is Value {value}<\li>\<ul>")    
# Create your views here.
