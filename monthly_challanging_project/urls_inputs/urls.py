from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>',views.monthly_redirect_by_no),
    path("<str:month_name>",views.monthbyname),
]
