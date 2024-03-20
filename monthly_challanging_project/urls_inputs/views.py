from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

month_challange={
    'january':"It's january monht no 1",
    'fabrury':"it's februry month no 2",
     'may':"it's may month no 5",
     'june':"it's june month no 6",
}
#or can try to add key as list  
'''
list_of_month=list(month_challange.keys())
if(month in list_of_month)
code..
'''

def monthly_redirect_by_no(request,month):
    list_of_month=list(month_challange.keys())
    if list_of_month[month]:
        return HttpResponseRedirect('/urls_inputs/'+ list_of_month[month])
    else:
        return HttpResponse("Months Not Found in inside collaction") #after adding this else statement except ret not required.
    
def monthbyname(request,month_name):
    try:
        ret = month_challange[month_name]
    except:
        ret = "not in app pls enter starting 5"
    return  HttpResponse(ret)        
    
# Create your views here.
