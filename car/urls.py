from django.urls import path

from .views import AddCar, GetCars, UpdateCarView

urlpatterns = [
    path('get-cars', GetCars.as_view(), name='get-cars'),
    path('add-cars', AddCar.as_view(), name='add-cars'),
    path('update-car/<str:car_id>/', UpdateCarView.as_view(), name='update-car'),

]
