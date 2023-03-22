from django.urls import path
from . import views
urlpatterns = [
    # path("home",views.home,name='home'),
    path('',views.user_login, name='user_login'),
    path("details", views.Employee_details, name='Employee_Data'),
 
]