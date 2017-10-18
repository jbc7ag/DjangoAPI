from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Personas
from .serializers import PersonasGetName,PersonasCreationSerializer, PersonasSerializer

import requests
import json
# Create your views here.

class PersonasApi(APIView):

    def get(self, request):
        personas=Personas.objects.all()
        serializer=PersonasSerializer(personas, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer=PersonasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self._sendPushNotification("Persona creada","fVSsKDAlnFY:APA91bF--nPb0yD7rYpLqfwFa306qdfORKK6plFbstHWr1gEWXBBXtVIxDtcqKPoya_AVsAdbMPPKmv7EpDXLPKbng-WUm9Gv9xbk_6ajB6ZHNegSWAlvjavMnkX_yJ61bRmZmMm-B2v")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _sendPushNotification(self, message, token):
        baseUrl="https://fcm.googleapis.com/fcm/send"
        headers={"Authorization":"key=AIzaSyB0k006LxEMxjpcL1bgz6CkAtEhX2UjQdY", "Content-Type":"application/json"}

        data={"notification": {"title": message,"body": "5 to 1","icon": "firebase-logo.png","click_action": "http://localhost:8081"},"to":token}
        data=json.dumps(data)
        pushnotification=requests.post(baseUrl,headers=headers, data=data)
        pushnotificationJSON=pushnotification.json()

        if pushnotification.status_code==200 and "error" not in pushnotificationJSON['results'][0]:
            return True
        else:
            return False


     #   if "error" in pushnotificationJSON["results"][0]:
      #      return False;






class PersonaApi(APIView):

    def _getPersona(self, pk):
        try:
              return Personas.objects.get(pk=pk)
        except Personas.DoesNotExists:
            raise status.HTTP_400_NOT_FOUND

    def get(self, request, pk):
        persona= self._getPersona(pk)
        serializer=PersonasSerializer(persona)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        persona=self._getPersona(pk)
        serializer=PersonasSerializer(persona,request.data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        persona=self._getPersona(pk)
        persona.delete();
        return Response(status=status.HTTP_204_NO_CONTENT)



