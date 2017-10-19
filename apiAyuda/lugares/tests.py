from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Lugares
from .serializers import *

import json

# Create your tests here.
#class LugaresTest(TestCase):

def setUp(self):
        self.client = Client()
        self.primer_lugar = Lugares.objects.create(calle="Prueba", nombre="nombre2", colonia="nuevacol")
        self.segundo_lugar = Lugares.objects.create(calle="Prueba", nombre="nombre2", colonia="nuevacol")


def test_get_all_lugares(self):
        response = self.client.get(reverse("lugares_endpoint"))
        lugares = Lugares.objects.all()
        serializer = LugaresSerializer(lugares, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

