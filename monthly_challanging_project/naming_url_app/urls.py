from django.urls import path

from . import views

urlpatterns = [
    path("<int:count>",views.func_name1),
    path("<str:name>",views.func_name2,name='naming_url'),
]
