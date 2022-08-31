from django.urls import path, include
from .viewsets import *

urlpatterns = [
    
    #API
    path('clients/', ClientsListViewSet.as_view(), name='client-list'),
    path('client/<uuid:pk>/', ClientDetailsViewSet.as_view(), name='client-detail'),
    path('client/categories/', ClientCategoriesListViewSet.as_view(), name='client-categories'),
]