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

from .models import *
from .serializers import *

class ServicesListViewSet(generics.ListCreateAPIView):
    http_method_names = ['post','get','put']
    serializer_action_classes = {
        'GET': ServiceViewSerializer,
        'POST': ServiceCreateSerializer,
    }
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.request.method]
        except(KeyError, AttributeError):
            return super().get_serializer_class()


    def get_queryset(self):
        """
        Returns a list of services for the current Business
        """
        user = self.request.user
        business= user.Business      
        
        return Service.objects.filter(Business=business)
class ClientsServiceViewSet(generics.ListCreateAPIView):
    http_method_names = ['post','get','put']
    serializer_action_classes = {
        'GET': ClientServiceViewSerializer,
        'POST': ClientCreateServiceSerializer,
    }
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.request.method]
        except(KeyError, AttributeError):
            return super().get_serializer_class()


    def get_queryset(self):
        """
        Returns a list of client Services of the current Business
        """
        user = self.request.user
        business= user.Business      
        
        return Client_Service.objects.filter(Business=business)

class InvoiceViewSet(generics.ListCreateAPIView):
    
    http_method_names = ['post','get','put']
    serializer_action_classes = {
        'GET': InvoiceViewSerializer,
        'POST': InvoiceCreateSerializer,
    }
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.request.method]
        except(KeyError, AttributeError):
            return super().get_serializer_class()

    def get_queryset(self):
        """
        Returns client invoices for the current Business
        """
        user = self.request.user
        business= user.Business     
        
        return Invoice.objects.filter(Business=business)
class ReceiptViewSet(generics.ListCreateAPIView):
    
    http_method_names = ['post','get','put']
    serializer_action_classes = {
        'GET': ReceiptViewSerializer,
        'POST': ReceiptCreateSerializer,
    }

    def get_queryset(self):
        """
        Returns client receipts for the current Business
        """
        user = self.request.user
        business= user.Business     
        
        return Receipt.objects.filter(Business=business)
class PayMethodViewSet(generics.ListCreateAPIView):
    
    http_method_names = ['post','get','put']
    serializer_action_classes = {
        'GET': PaymentMethodViewSerializer,
        'POST': PaymentMethodCreateSerializer,
    }

    def get_queryset(self):
        """
        Returns a list of payment methods for the current Business
        """
        user = self.request.user
        business= user.Business     
        
        return Payment_Method.objects.filter(Business=business)