from accounts.serializers import BusinessSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from .serializers import LoginSerializer, RegistrationSerializer
from django.utils.decorators import method_decorator


#@method_decorator(csrf_exempt, name='dispatch')
class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post', ] 
     
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegistrationView(ModelViewSet, TokenObtainPairView):
    serializer_class = RegistrationSerializer    
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
           # refresh = RefreshToken.for_user(serializer)
           # res = {
           # "refresh": str(refresh),
           # "access": str(refresh.access_token),
           #  }

            return Response({
            "user": serializer.data,            
            #"refresh": res["refresh"],
            #"token": res["access"]
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    permission_classes = [AllowAny,]
    http_method_names = ['post',]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception = True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)