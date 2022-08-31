#from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.base import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
import uuid

import jwt
from datetime import datetime,timedelta
from django.conf import settings


#from users.models import User
 #Create your models here.
#The accounts models will deal with registration and management of user and busines accounts
"""
An account is the base model that owns all other models. Each Model must reference the account model
"""
class Business (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business_name = models.CharField(max_length=100, unique=True)    

      
    def __str__(self):
        return self.business_name


class BusinessAwareModel(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)

    class Meta:
        abstract = True
class UserManager(BaseUserManager):
    """
    A custom user model manager where email is the unique identifier
    for authentication instead of username.
    """
    use_in_migrations=True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password
        """
      
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superUser with the given email and password
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('Business_id','f933e03b-5b29-4b7b-99ab-af6ee888f791')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(email, password, **extra_fields)

#Custom user object
class User(AbstractBaseUser, PermissionsMixin, BusinessAwareModel):
    """
    Custom user model that extends Django's AbstractUser model. It uses the email as the username

    email and password are required. Other fields are optional.

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active=models.BooleanField(_('active'), default=True)
    is_staff=models.BooleanField(_('staff'), default=False)
    is_owner=models.BooleanField(_('owner'), default=False)
    signup_confirmation = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()
    
    def _generate_jwt_token(self):
         """
         Generates a JSON Web Token that stores this user's ID and has an expiry
         date set to 60 days into the future.
         """
        # dt = datetime.now() + timedelta(days=60)

         token= jwt.encode({
             'id': str(self.pk),
             'exp': datetime.now()+ timedelta(days=60)
             #dt.utcfromtimestamp(dt.timestamp())
            
         }, settings.SECRET_KEY, algorithm='HS256')

         return token.decode('utf-8')
        
        
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this user.

        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
   
    def __str__(self):
        return self.email

