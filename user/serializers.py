from rest_framework import serializers

from car.models import Purchase
from utils.validator import check_phone_number, check_avatar, check_car_image


class GetOtpDeserializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)

    @staticmethod
    def validate_phone_number(obj):
        check_phone_number(obj)
        return obj


class VerifyDeserializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    otp = serializers.CharField(required=True)


class UpdateProfileDeserializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    avatar = serializers.ImageField(required=True)

    def validate_avatar(self, obj):
        check_avatar(obj)
        return obj


class PurchaseDeserializer(serializers.Serializer):
    wallet_number = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)
    order = serializers.BooleanField(required=True)
    purchase_id = serializers.CharField(required=True)


class SelectedCarDeserializer(serializers.Serializer):
    car_id = serializers.CharField(required=True)


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class CreateCarDeserializer(serializers.Serializer):
    category_id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    brand = serializers.CharField(required=True)
    color = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    image = serializers.ImageField(required=True)

    def validate_image(self, obj):
        check_car_image(obj)
        return obj
