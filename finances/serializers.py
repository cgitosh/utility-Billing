from dataclasses import fields
from accounts.serializers import BusinessAwareSerializer
from clients.serializers import ClientViewSerializer
from .models import Client
from .models import *
from rest_framework import serializers


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','service_name','Business','user',]

class ServiceViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = BusinessAwareSerializer.Meta.fields +['id','service_name','user',]

class ClientCreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Service
        fields = ['id','client','service','monthly_charge','user','Business',]

class ClientServiceViewSerializer(BusinessAwareSerializer, serializers.ModelSerializer):

    user=serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = Client_Service
        fields = BusinessAwareSerializer.Meta.fields +['id','client','service','monthly_charge','user',]

class InvoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'inv_no', 'client', 'invoice_amount','invoice_balance','extra_charges','invoice_date','user','Business',]

class InvoiceViewSerializer(BusinessAwareSerializer, serializers.ModelSerializer):
    client = ClientViewSerializer()
    class Meta:
        model = Invoice
        fields = BusinessAwareSerializer.Meta.fields +['id', 'inv_no', 'client', 'invoice_amount','invoice_balance','extra_charges','invoice_date','user',]    

class PaymentMethodCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Method
        fields = ['id','method_name', 'user','Business']

class PaymentMethodViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Method
        fields = BusinessAwareSerializer.Meta.fields +['id','method_name','user',]    

class ReceiptCreateSerializer(BusinessAwareSerializer, serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['id', 'recpt_no', 'invoice', 'amount_paid','receipt_date','user','Business',]

class ReceiptViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields =BusinessAwareSerializer.Meta.fields + ['id', 'recpt_no', 'invoice', 'amount_paid','receipt_date','user',]
