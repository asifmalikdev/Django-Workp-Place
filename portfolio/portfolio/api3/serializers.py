from rest_framework import serializers

class Api3Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    fname = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)