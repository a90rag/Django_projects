from django.urls import path

from . import views

urlpatterns = [
    path("january",views.january),
    path("februry",views.februry),
    path('<month>',views.month_name),
]
