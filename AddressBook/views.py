from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics,permissions



#To Read Address from db
@api_view(['GET'])
def Address(request):
    queryset=AddressB.objects.all()
    serializer=AddressBSerializer(queryset,many=True)
    return Response(serializer.data)

#To create new Address in db
@api_view(['POST'])
def PostAD(request):
    queryset=AddressB.objects.all()
    serializer=AddressBSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


 #To update Address in db  
@api_view(['POST'])
def UpdateAD(request,id):
    queryset=AddressB.objects.get(id=id)
    serializer=AddressBSerializer(instance=queryset,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#to delete address from db
@api_view(['DELETE'])
def DeleteAD(request,id):
    queryset=AddressB.objects.get(id=id)
    queryset.delete()
    return Response("Address is deleted")


















# from rest_framework import status
# from rest_framework.views import APIView
# # from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from AddressBook.models import AddressB
# from AddressBook.serializers import AddressBSerializer


# class AddressBlistAV(APIView):
#     def get(self,request):
#         queryset=AddressB.objects.all()
#         serializer=AddressBSerializer(queryset,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=AddressBSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
# class AddressBdetailAV(APIView):
#     def get(self,request):
#         try:
#             queryset=AddressB.objects.get(pk=pk)
#         except AddressB.DoesNotExist:
#             return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer=AddressBSerializer(queryset)
#         return Response(serializer.data)         
    
    
#     def put(self,request):
#         queryset=AddressB.objects.get(pk=pk)
#         serializer=AddressBSerializer(queryset,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(request,pk):
#         queryset=AddressB.objects.get(pk=pk)
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
 

