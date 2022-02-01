from django.urls import path
from medcoadmin import views

urlpatterns = [
    path('',views.dash_bd,name="dashboard"),
    path('user/',views.user,name="user"),
    path('user_permisson/',views.user_per,name="user_per"),
    path('add_order/',views.add_order,name="add_od"),
]