from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import CreditCard
from .serializers import CreditCardSerializer, AlchemyCreditCardSerializer
from DBAPI import Session


# Create your views here.
def hello(request):
    return HttpResponse("Hello")


@api_view(['GET', 'POST'])
def get_post_CreditCard(request):
    # get all credit cards
    if request.method == 'GET':
        cards = CreditCard.objects.all()
        serializer = CreditCardSerializer(cards, many=True)
        return Response(serializer.data)
    # insert a new record for a credit card
    elif request.method == 'POST':
        data = request.data
        serializer = CreditCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def create_AlchemyCreditCard(request):
    # # get all credit cards
    # if request.method == 'GET':
    #     session = Session()
    #     session.query(Alchemy)
    #     serializer = CreditCardSerializer(cards, many=True)
    #     return Response(serializer.data)
    # insert a new record for a credit card
    if request.method == 'POST':
        data = request.data
        serializer = AlchemyCreditCardSerializer(data=data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if serializer.is_valid():
        #     serializer.save(serializer.validated_data)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
