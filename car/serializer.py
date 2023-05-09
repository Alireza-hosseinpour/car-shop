from rest_framework import serializers

from car.models import Car


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'price']
        # exclude = ('uuid', 'otp', 'otp_expire_at')


class UpdateCarDeserializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    brand = serializers.CharField(required=True)
    color = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    image = serializers.ImageField(required=True)
