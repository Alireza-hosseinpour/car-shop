from django.urls import path

from .views import PurchaseView , PaymentView

urlpatterns = [
    path('purchase-order', PurchaseView.as_view(), name='purchase'),
    path('payment', PaymentView.as_view(), name='payment')
]
