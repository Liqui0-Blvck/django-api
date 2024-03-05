from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import *

# Create your views here.


class ComercializadorViewSet(ModelViewSet):
  queryset = Comercializador.objects.all()
  serializer_class = ComercializadorSerializer
  
  