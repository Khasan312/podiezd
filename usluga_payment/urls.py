from django.urls import path

from .views import home, index, json

urlpatterns = [
    path("", index, name="index"),
    path('home', home, name='home'),
    path('json', json, name='json')
]
