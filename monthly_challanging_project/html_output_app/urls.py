from django.urls import path
from . import views

urlpatterns = [

path("<int:value>",views.func_name1,name="name1"),
path("<str:value>s",views.func_name2,name="name2"),
]