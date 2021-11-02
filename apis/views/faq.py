from django.shortcuts import render
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from apis.models.faq import Faq
# repositories
from apis.repositories.baseRepository import getList
# seriializers
from apis.serializers.faq import FaqSerializer

@api_view(['GET'])
def faqs(request):
	faqs = getList(Faq)
	serializer = FaqSerializer(faqs, many=True)
	return Response(serializer.data)