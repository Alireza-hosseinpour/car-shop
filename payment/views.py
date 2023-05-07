from datetime import datetime
from utils.custom_response import invalid_response, successful_response, car_not_found_response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import SelectedCarDeserializer, PurchaseDeserializer, PurchaseSerializer
from utils.authenticate import Authenticate
from car.models import Purchase, Car
from utils.purchase_handler import get_car_if_exist, save_purchase


class PurchaseView(APIView):
    def post(self, request, *args, **kwargs):
        user = Authenticate.get_user_with_token(request)
        data = SelectedCarDeserializer(data=request.data)
        if not data.is_valid():
            return invalid_response(data.errors)
        car = get_car_if_exist(data.validated_data.get('car_id', None))
        if not car:
            return car_not_found_response()
        purchase = save_purchase(user, car)
        serializer = PurchaseSerializer(purchase, many=False)
        return successful_response(serializer.data)


class PaymentView(APIView):
    # miss this step doesn't need yet but not bad
    def post(self, request, *args, **kwargs):
        user = Authenticate.get_user_with_token(request)
        data = PurchaseDeserializer(data=request.data)

        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        # if user:
        if data.validated_data.get("order", None):
            wallet_number = data.validated_data.get("wallet_number", None)
            amount = data.validated_data.get("amount", None)
            purchase_id = data.validated_data.get("purchase_id", None)
            purchase = Purchase.objects.get(id=purchase_id)
            if amount == purchase.car.price:
                purchase.purchase_date = datetime.now()
                purchase.is_delivered = True
                purchase.is_paid = True
                purchase.save()
                return Response("Successful purchase", status=status.HTTP_200_OK)
