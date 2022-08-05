from rest_framework import serializers

class LocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    
class LocationUpdateSerializer(serializers.Serializer):
    old_name = serializers.CharField(max_length=30)
    new_name = serializers.CharField(max_length=30)