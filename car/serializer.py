from rest_framework import serializers

from car.models import Car


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'price']
        # exclude = ('uuid', 'otp', 'otp_expire_at')
