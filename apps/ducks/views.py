from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Duck
from .serializer import Duckserializer
from django.shortcuts import get_object_or_404


class Ducklist(generics.ListCreateAPIView):
    queryset = Duck.objects.all()
    serializer_class = Duckserializer
    def get_object(self):
        queryset=self.get_queryset
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk']
         )
        return obj