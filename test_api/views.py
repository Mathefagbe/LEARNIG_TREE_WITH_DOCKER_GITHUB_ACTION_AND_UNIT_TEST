from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class TrackApiView(APIView):

    def post(self,request):
        try:
            serializer=TrackSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        

class GenreApiView(APIView):

    def post(self,request):
        try:
            serializer=GenreSerailizer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            instance=Genre.objects.all()
            data=GenreSerailizer(instance,many=True).data
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

class SingleTrackApiView(APIView):

    def put(self,request,pk):
        try:
            instance=Track.objects.get(pk=pk)
            serializer=TrackSerializer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,pk):
        try:
            instance=Track.objects.get(pk=pk)
            data=TrackSerializer(instance).data
            return Response(data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)


class SingleGenreApiView(APIView):

    def put(self,request,pk):
        try:
            instance=Genre.objects.get(pk=pk)
            serializer=GenreSerailizer(instance=instance,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,pk):
        try:
            instance=Genre.objects.get(pk=pk)
            data=GenreSerailizer(instance).data
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)