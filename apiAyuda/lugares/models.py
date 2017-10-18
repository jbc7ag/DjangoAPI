from django.db import models

from personas.models import Personas

STATUS=(("1","Activo"),("0","Inactivo"))

# Create your models here.
class Lugares(models.Model) :
    calle = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)

class PersonasHasLugares(models.Model):
    fecha = models.DateField()
    status = models.CharField(choices=STATUS,max_length=100)
    lugares_id = models.ForeignKey(Lugares)
    personas_id = models.ForeignKey(Personas)

