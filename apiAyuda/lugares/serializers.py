from rest_framework import serializers
from .models import Lugares , PersonasHasLugares




class LugaresGetName(serializers.Serializer) :
    nombre = serializers.CharField(max_length=100)


class LugaresCreationSerializer(serializers.Serializer) :
    calle = serializers.CharField(max_length=100)
    nombre = serializers.CharField(max_length=100)
    colonia = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Lugares.objects.create(**validated_data)

class LugaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = ['calle','nombre','colonia','id']


class LugaresHasPersonasGet(serializers.Serializer) :
    fecha = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)
    lugares_id = serializers.CharField(max_length=100)
    personas_id=serializers.CharField(max_length=100)


class LugaresHasPersonasSerializer(serializers.ModelSerializer):

     lugares_id =  serializers.StringRelatedField()

     class Meta:
         model = PersonasHasLugares
         fields = ['fecha','status','lugares_id','personas_id']

