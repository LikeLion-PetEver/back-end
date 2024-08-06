from rest_framework import serializers
from .models import Funeral, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['lat', 'lng']

class FuneralSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Funeral
        fields = ['id', 'name', 'region', 'address', 'phone', 'image', 'website', 'created_at', 'location']

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        funeral = Funeral.objects.create(location=location, **validated_data)
        return funeral
