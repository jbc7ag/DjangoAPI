from django.db import models

# Create your models here.

SEXOS=(("M","Mujer"),("H","Hombre"),("I","Indefinido"))
TIPOSPERSONAS=(("Voluntario","Voluntario"),("Damnificado","Damnificado"),("Otro","Otro"))


class Personas(models.Model) :
    nombre = models.CharField(max_length=100)
    edad=models.IntegerField()
    sexo=models.CharField(choices=SEXOS,max_length=5)
    tipo_de_persona=models.CharField(choices=TIPOSPERSONAS,max_length=50)


