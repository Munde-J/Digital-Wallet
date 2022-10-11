from msilib.schema import Class
from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
 queryset = Customer.objects.all()
 serializer_class = CustomerSerializer



# Create your views here.
