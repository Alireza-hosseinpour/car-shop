from django.urls import path

from user import views

urlpatterns = [
    path('get-otp', views.GetOtp.as_view(), name='get-otp'),
    path('verify-otp', views.VerifyOtp.as_view(), name='verify-otp'),
    path('update-profile', views.UpdateProfile.as_view(), name='update-profile')
]
