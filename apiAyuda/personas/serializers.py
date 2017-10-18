from rest_framework import serializers
from .models import Personas

SEXOS=(("M","Mujer"),("H","Hombre"),("I","Indefinido"))
TIPOSPERSONAS=(("Voluntario","Voluntario"),("Damnificado","Damnificado"),("Otro","Otro"))

def validar_edad(source):
    if source > 100:
        raise serializers.ValidationError("No hay nadie mayor a 100")



class PersonasGetName(serializers.Serializer) :
    nombre = serializers.CharField(max_length=100)


class PersonasCreationSerializer(serializers.Serializer) :
    nombre = serializers.CharField(max_length=100)
    edad=serializers.IntegerField(validators=[validar_edad])
    sexo=serializers.CharField(max_length=5)
    tipo_de_persona=serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Personas.objects.create(**validated_data)

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['nombre','edad','sexo','tipo_de_persona','id']


class PersonasModifySerializer(serializers.Serializer):
        tipo_de_persona = serializers.CharField( max_length=50)