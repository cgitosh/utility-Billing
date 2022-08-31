from django.db.models import base
#from django.db import router
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


from .viewsets import UserListViewSet, UserDetailViewset,BusinessListViewSet, BusinessDetailViewSet,api_root
from .auth.viewsets import LoginViewSet, RegistrationView, RefreshViewSet

router = routers.SimpleRouter()
router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegistrationView, basename='register')
router.register(r'refresh', RefreshViewSet, basename='refresh')

urlpatterns = [ 
    #API    
    path('', api_root),
    path('user/', UserListViewSet.as_view(), name='user-list'),
    path('user/<uuid:pk>/', UserDetailViewset.as_view(), name='user-detail'),
    path('business/', BusinessListViewSet.as_view(), name='business-list'),
    path('business/<uuid:pk>/', BusinessDetailViewSet.as_view(), name='business-detail'),  
    path('auth/', include(router.urls), name='auth-provider'),      
]
urlpatterns = format_suffix_patterns(urlpatterns)