from accounts.models import BusinessAwareModel
from accounts.serializers import BusinessAwareSerializer
from .models import Client, category
from rest_framework import serializers


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id','category_name','monthly_charge','Business','user',]

class CategoryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = BusinessAwareSerializer.Meta.fields +['id','category_name','monthly_charge','user',]

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','house_no','category','first_name','last_name','mobile_no','address','user','Business',]

class ClientViewSerializer(BusinessAwareSerializer, serializers.ModelSerializer):

    user=serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    category = CategoryViewSerializer()
    class Meta:
        model = Client
        fields = BusinessAwareSerializer.Meta.fields +['id','category','house_no','first_name','last_name','mobile_no','address','user',]

