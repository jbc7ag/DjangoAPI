from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Lugares,PersonasHasLugares
from .serializers import LugaresGetName,LugaresCreationSerializer, LugaresSerializer,LugaresHasPersonasSerializer,LugaresHasPersonasGet

# Create your views here.

class LugaresApi(APIView):

    def get(self, request):
        lugares=Lugares.objects.all()
        serializer=LugaresGetName(lugares, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer=LugaresCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LugareshasPersonaApi(APIView):

    def get(self, request):
        lugares=PersonasHasLugares.objects.all()
        serializer=LugaresHasPersonasGet(lugares, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer=LugaresHasPersonasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

