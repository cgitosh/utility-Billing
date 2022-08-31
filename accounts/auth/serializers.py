#from typing_extensions import Required
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist

from ..serializers import BusinessSerializer, UserSerializer
from ..models import Business, User

class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data= super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['business'] = BusinessSerializer(self.user.Business).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data



  
class RegistrationSerializer(serializers.ModelSerializer):
  
    #user=UserSerializer()
    Business=BusinessSerializer()
    #business_detail = BusinessSerializer(source='Business', read_only=True)
    password = serializers.CharField(max_length = 128, min_length=8, write_only=True, required=True, style={'input_type': 'password'})
    #password2 = serializers.CharField(max_length = 128, min_length=8, write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(
            required=True, write_only=False, max_length=128,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model=User
        fields=  ['id','first_name','last_name','email','avatar','password','Business','token',] 
    def create(self, validated_data):
        business_data= validated_data.pop('Business')
        business=Business.objects.create(**business_data)
        #for user in user_data:
        user=User.objects.create_user(Business=business, **validated_data)
        user.is_active=True
        user.is_owner=True
        user.is_staff=True
        user.is_superuser=True
        user.signup_confirmation=True #Later to be replaced with a confirmation email 
        user.save()
        return user  
         
class UserRegistrationSerializer(UserSerializer):
    password1 = serializers.CharField(max_length = 128, min_length=8, write_only=True, required=True)
    password2 = serializers.CharField(max_length = 128, min_length=8, write_only=True, required=True)
    email =  serializers.EmailField(required=True, write_only = True, max_length=128)
    
    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model=User
        fields= ['first_name','last_name','email','password1','password2']
    
    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user=User.objects.create_user(**validated_data) 
        return user
class BusinessRegistrationSerializer(BusinessSerializer):

    class Meta:
        model=Business
        fields = ['business_name']