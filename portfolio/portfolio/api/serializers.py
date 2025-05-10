from rest_framework import serializers
from .models import Student as MyAppStudent
class StudentSerialziser(serializers.ModelSerializer):
    class Meta:
        model = MyAppStudent
        fields = ['id', 'name', 'roll', 'city']
    # def create(self, validated_data):
    #     return MyAppStudent.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     print("before update",instance.name)
    #     instance.name = validated_data.get('name', instance.name)
    #     print('after update',instance.name)
    #     instance.roll=validated_data.get('roll', instance.roll)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.save()
    #     return instance


class StudentDummySerializer(serializers.Serializer):
    nam=serializers.CharField(max_length=30)
    fnam = serializers.CharField(max_length=30)