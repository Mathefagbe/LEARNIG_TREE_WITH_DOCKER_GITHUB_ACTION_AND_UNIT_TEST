from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializers import CreateAccountSerializer,CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class RegisterAPiView(APIView):
    authentication_classes=[]
    permission_classes=[]

    def post(self,request):
        try:
            serializer=CreateAccountSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)



class CustomTokenObtainPairViewSet(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes=[]
    authentication_classes=[]
 
    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)