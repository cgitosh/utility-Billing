from django.contrib.auth import authenticate
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import exceptions, serializers
from .models import User,Business,BusinessAwareModel
from rest_framework_simplejwt.serializers import TokenObtainSerializer
#from django.utils.translation import gettext_lazy as _


class BusinessSerializer(serializers.ModelSerializer):

    #url=serializers.HyperlinkedIdentityField(view_name='business-detail', read_only=True)
    class Meta:
        model = Business
        fields = ['id','business_name']

class BusinessAwareSerializer(serializers.Serializer):

    Business= serializers.UUIDField(read_only=True)

    class Meta:
        fields=['Business']
    

    class Meta:
        model=BusinessAwareModel
        fields=['Business']
    

class UserSerializer(BusinessAwareSerializer, serializers.ModelSerializer):
    
    #url = serializers.HyperlinkedIdentityField(view_name='user-detail', read_only=True)

    class Meta:
        model = User
        fields= BusinessAwareSerializer.Meta.fields + ['id','first_name','last_name','email','date_joined', 'avatar']
    
    def create(self, validated_data):
        #Create business
        New_business= Business.objects.create(**validated_data)
        #get the business
        business = Business.objects.get(Business=New_business)

        #create a user and pass the business
        #User.objects.create(**validated_data, Business=business)
        user = User.objects.create_user(**validated_data)
               
        return user
       
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        email = data.get('email', None)
        password = data.get('password', None)

        # Raise an exception if an
        # email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value since in our User
        # model we set `USERNAME_FIELD` as `email`.
        user = authenticate(username=email, password=password)

        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag is to tell us whether the user has been banned
        # or deactivated. This will almost never be the case, but
        # it is worth checking. Raise an exception in this case.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'email': user.email,
            'token': user.token
        }
