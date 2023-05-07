from rest_framework.views import APIView
from .models import Car
from utils.authenticate import Authenticate
from user.serializers import CreateCarDeserializer
from utils.check_car_info import save_car
from .serializer import CarsSerializer
from utils.custom_response import successful_response, user_not_found_response, invalid_response, \
    car_created_response


class GetCars(APIView):

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return successful_response(serializer.data)


class AddCar(APIView):
    def post(self, request, *args, **kwargs):
        user = Authenticate.get_user_with_token(request)
        if not user:
            return user_not_found_response()
        data = CreateCarDeserializer(data=request.data)
        if not data.is_valid():
            return invalid_response(data.errors)

        save_car(data)
        return car_created_response()
