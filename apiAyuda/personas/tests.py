from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Personas
from .serializers import *

import json

# Create your tests here.

class PersonasTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.primer_persona= Personas.objects.create(nombre="Prueba", edad=33, sexo="M",tipo_de_persona="Voluntario")
        self.segunda_persona = Personas.objects.create(nombre="Prueba 1",edad=33, sexo="M",tipo_de_persona="Voluntario")

        self.persona_correcta_json={"nombre" : "Prueba 1","edad" : "33","sexo" : "M","tipo_de_persona" : "Voluntario"}
        self.persona_incorrecta_json = {"nombre" : "Prueba 1","edad" : "33","sexo" : "M", "tipo_de_persona" : "Voluntario"}



    def test_get_all_personas(self):
        response =self.client.get(reverse("personas_endpoint"))
        personas = Personas.objects.all()
        serializer = PersonasSerializer(personas, many=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(serializer.data,response.data)


    def test_get_one_person(self):
        response=self.client.get(reverse('persona_endpoint', kwargs={'pk':self.primer_persona.id}))
        persona=Personas.objects.get(pk=self.primer_persona.id)
        serializer=PersonasSerializer(persona)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)


    def test_post_persona(self):
        response=self.client.post(reverse('personas_endpoint'),
                                  data=json.dumps(self.persona_correcta_json),
                                  content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_delete_persona(self):
        response = self.client.delete(reverse('persona_endpoint', kwargs={'pk':self.segunda_persona.id}))
        self.assertEqual(response.status_code, 200)


    def test_put_persona(self):
        response= self.client.put(reverse('persona_endpoint',
                                  kwargs={'pk':self.primer_persona.id}),
                                  data=json.dumps(self.persona_correcta_json),
                                  content_type='application/json')
        self.assertEqual(response.status_code,202)

