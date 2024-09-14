
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('athlete_list/', views.athlete_list, name="athlete_list"),
     path('athletes/<str:country>/', views.athlete_list_country, name='athlete_list_country'),
]
