from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import viewsets

class ProducttableViewSet(viewsets.ModelViewSet):
    queryset = Producttable.objects.all();
    serializer_class = ProducttableSerializer

class ProductCreateView(APIView):
    def get(self,request):
        products=Producttable.objects.all()
        serializer=ProducttableSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProducttableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



