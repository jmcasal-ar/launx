from django.urls import path
from .views import HomePageView
 
urlpatterns = [
 
    #Paths del core
    path('', HomePageView.as_view(), name="home"),
]
