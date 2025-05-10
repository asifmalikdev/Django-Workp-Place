from rest_framework import serializers

class StudentsSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    clas = serializers.IntegerField()
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=30)