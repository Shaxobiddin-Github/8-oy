from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Klass, Mexmonxona, Travel
from .serializers import KlassSerializer, MexmonxonaSerializer, TravelSerializer

# Klass API
class KlassAPIView(APIView):
    def get(self, request):
        klasslar = Klass.objects.all()
        serializer = KlassSerializer(klasslar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KlassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KlassDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Klass.objects.get(pk=pk)
        except Klass.DoesNotExist:
            return None

    def get(self, request, pk):
        klass = self.get_object(pk)
        if klass is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = KlassSerializer(klass)
        return Response(serializer.data)

    def put(self, request, pk):
        klass = self.get_object(pk)
        if klass is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = KlassSerializer(klass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        klass = self.get_object(pk)
        if klass is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        klass.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Mexmonxona API
class MexmonxonaAPIView(APIView):
    def get(self, request):
        mexmonxonalar = Mexmonxona.objects.all()
        serializer = MexmonxonaSerializer(mexmonxonalar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MexmonxonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MexmonxonaDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Mexmonxona.objects.get(pk=pk)
        except Mexmonxona.DoesNotExist:
            return None

    def get(self, request, pk):
        mexmonxona = self.get_object(pk)
        if mexmonxona is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MexmonxonaSerializer(mexmonxona)
        return Response(serializer.data)

    def put(self, request, pk):
        mexmonxona = self.get_object(pk)
        if mexmonxona is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MexmonxonaSerializer(mexmonxona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mexmonxona = self.get_object(pk)
        if mexmonxona is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        mexmonxona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Travel API
class TravelAPIView(APIView):
    def get(self, request):
        travels = Travel.objects.all()
        serializer = TravelSerializer(travels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TravelDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return None

    def get(self, request, pk):
        travel = self.get_object(pk)
        if travel is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TravelSerializer(travel)
        return Response(serializer.data)

    def put(self, request, pk):
        travel = self.get_object(pk)
        if travel is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TravelSerializer(travel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        travel = self.get_object(pk)
        if travel is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        travel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
