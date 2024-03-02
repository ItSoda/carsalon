from rest_framework import serializers
from .models import Car, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image")


class CarSerializer(serializers.ModelSerializer):
    photos = ImageSerializer(many=True)
    class Meta:
        model = Car
        fields = "__all__"