from django.urls import path

from travel_app import views

urlpatterns = [
    path('', views.index, name="index")
]
