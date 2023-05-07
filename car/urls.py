from django.urls import path

from .views import AddCar, GetCars

urlpatterns = [
    path('get-cars', GetCars.as_view(), name='get-cars'),
    path('add-cars', AddCar.as_view(), name='add-cars'),
]
