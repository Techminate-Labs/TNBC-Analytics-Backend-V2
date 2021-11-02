from django.shortcuts import render
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from apis.models.donate import Donate
# repositories
from apis.repositories.baseRepository import getList
# seriializers
from apis.serializers.donate import DonateSerializer

@api_view(['GET'])
def donates(request):
	donates = getList(Donate)
	serializer = DonateSerializer(donates, many=True)
	return Response(serializer.data)