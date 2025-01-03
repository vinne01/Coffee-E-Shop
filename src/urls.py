
from django.urls import path
from .views import home ,success,menu

urlpatterns = [
    path('home/',home,name="home"),
    path('success/',success,name="success"),
    path('',menu,name="menu")
  
]