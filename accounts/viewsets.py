from django.http.request import HttpHeaders
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters, generics
from rest_framework.views import APIView
from .serializers import BusinessAwareSerializer, UserSerializer, BusinessSerializer,LoginSerializer
from .models import Business, BusinessAwareModel, User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,permissions,viewsets
from rest_framework.reverse import reverse

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, JWTAuthentication
from rest_framework.settings import api_settings



@api_view(['GET', 'POST'])
def api_root(request, format=None):

    return Response({
        'login': reverse('login-list', request=request, format=format),
        'register': reverse('register-list', request=request, format=format),
        'Users': reverse('user-list', request=request, format=format),
        'Business': reverse('business-list', request=request, format=format),
        #'Cargo': reverse('cargo-list', request=request,format=format),
        #'Cargo UOM':reverse('cargouom-list',request=request, format=format),
        #'Cargo Category':reverse('cargocategory-list',request=request, format=format),
        #'Cargo Sub Category':reverse('cargosub-category-list',request=request, format=format),
        #'Route': reverse('route-list', request=request, format=format),
        #'Distance UOM': reverse('distanceuom-list',request=request, format=format),
       
        #'Truck Type': reverse('trucktype-list',request=request, format=format),
        #'Trucks':reverse('truck-list',request=request, format=format),
        #'Crew Category':reverse('crewcategory-list',request=request, format=format),
        #'Crew':reverse('crew-list',request=request, format=format),
        'Consignments':reverse('consignment-list',request=request, format=format),
        'Consignment Category': reverse('consignmentcat-list',request=request, format=format),
        'Consignment Status': reverse('consignmentstatus-list',request=request, format=format),
        'Client':reverse('client-list',request=request, format=format),
        

        



    })

class UserListViewSet(generics.ListAPIView):
    """
    List all users or create a new user
    """    
    serializer_class = UserSerializer
    
    
    def get_queryset(self):
        """
        This view should return a list of all User accounts
        for the currently authenticated Business.
        """
        user = self.request.user
        business= user.Business      
        
        return User.objects.filter(Business=business)
  

class UserDetailViewset(generics.RetrieveUpdateDestroyAPIView):
    #queryset = User.objects.all()
    serializer_class=UserSerializer

    def get_queryset(self):
        """
        This view should return a list of all User accounts
        for the currently authenticated Business.
        """
        user = self.request.user
        business= user.Business      
        
        return User.objects.filter(Business=business)

class BusinessListViewSet(generics.ListCreateAPIView):
    #queryset= Business.objects.all()
    serializer_class=BusinessSerializer

    def get_queryset(self):
        """
        Returns the business of the currently logged in user
        """
        user = self.request.user
        business= user.Business.id      
        
        return Business.objects.filter(id=business)

class BusinessDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
   # queryset = Business.objects.all()
    serializer_class=BusinessSerializer

    def get_queryset(self):
        """
        Returns the business of the currently logged in user
        """
        user = self.request.user
        business= user.Business.id      
        
        return Business.objects.filter(id=business)

