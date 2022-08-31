from accounts.models import Business
from django.http import HttpResponse, JsonResponse
from django.http.response import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from .models import Client
from .serializers import *

class ClientCategoriesListViewSet(generics.ListCreateAPIView):
    http_method_names = ['post','get','put']
    serializer_action_classes = {
        'GET': CategoryViewSerializer,
        'POST': CategoryCreateSerializer,
    }
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.request.method]
        except(KeyError, AttributeError):
            return super().get_serializer_class()


    def get_queryset(self):
        """
        Returns a list of client categories for the current Business
        """
        user = self.request.user
        business= user.Business      
        
        return category.objects.filter(Business=business)

class ClientsListViewSet(generics.ListCreateAPIView):
    http_method_names = ['post','get','put']
    serializer_action_classes = {
        'GET': ClientViewSerializer,
        'POST': ClientCreateSerializer,
    }
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.request.method]
        except(KeyError, AttributeError):
            return super().get_serializer_class()


    def get_queryset(self):
        """
        Returns a list of clients for the current Business
        """
        user = self.request.user
        business= user.Business      
        
        return Client.objects.filter(Business=business)

class ClientDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class=ClientViewSerializer

    def get_queryset(self):
        """
        Returns client details for the current Business
        """
        user = self.request.user
        business= user.Business     
        
        return Client.objects.filter(Business=business)