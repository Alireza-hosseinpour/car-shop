from django.urls import path

from . import views

urlpatterns = [
    path('admin/', views.AdminPanelView.as_view(), name='admin'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('delete/<str:user_id>/', views.DeleteView.as_view(), name='delete'),
    path('delete-car/<str:car_id>/', views.DeleteCarView.as_view(), name='delete-car'),
    path('logout/', views.Logout, name='logout'),
    path('update/<str:user_id>/', views.UpdateUserView.as_view(), name='update-user'),
    path('listofusers/', views.ListOfUsers.as_view(), name='list-of-users'),
    path('listofcars/', views.ListOfCars.as_view(), name='list-of-cars'),
    path('update-car/<str:car_id>/', views.UpdateCarView.as_view(), name='update-car'),
    path('purchaselist/', views.PurchaseList.as_view(), name='purchase-list'),
    path('update-purchase/<str:purchase_id>/', views.PurchaseUpdateView.as_view(), name='purchase-update'),
    path('add-car/', views.AddCarView.as_view(), name='add-car'),


]
