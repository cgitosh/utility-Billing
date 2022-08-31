from django.urls import path, include
from .viewsets import *

urlpatterns = [
    
    #API
    path('services/', ServicesListViewSet.as_view(), name='client-list'),
    path('service/<uuid:pk>/', ServicesListViewSet.as_view(), name='client-detail'),
    path('clientservices/', ClientsServiceViewSet.as_view(), name='Client-Services'),
    path('invoices/', InvoiceViewSet.as_view(), name='client-invoices'),
    path('invoice/<uuid:pk>/',InvoiceViewSet.as_view(), name='Invoice-Detail'),
    path('receipts/',ReceiptViewSet.as_view(), name='Client-receipts'),
    path('receipt/<uuid:pk>/',ReceiptViewSet.as_view(), name='Receipt-Detail'),
    path('paymethods/',PayMethodViewSet.as_view(), name='Pay-methods'),

] 