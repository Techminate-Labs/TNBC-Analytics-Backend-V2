from django.shortcuts import render
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from apis.models.profile import Profile
# repositories
from apis.repositories.baseRepository import getList
# seriializers
from apis.serializers.profile import ProfileSerializer

@api_view(['GET'])
def profiles(request):
	profiles = getList(Profile)
	serializer = ProfileSerializer(profiles, many=True)
	return Response(serializer.data)