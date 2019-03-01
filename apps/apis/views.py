from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from apps.ducks.models import Duck
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    )
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
    
)
from .serializer import (
    ListDucksSerializers,
    allDucksSerializers,
    OnefieldSerializer,
    CreateSerializers
    )
from rest_framework.permissions import(
    AllowAny , 
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

class DuckList(ListAPIView):
    queryset = Duck.objects.all()
    serializer_class= ListDucksSerializers
    permission_classes = [IsAuthenticated,IsAdminUser]


class DuckDetail_pk(RetrieveAPIView):
    queryset = Duck.objects.all()
    serializer_class = ListDucksSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    

class DuckDetail(DuckDetail_pk):
    
    lookup_field='nombre'#es por donde el buscara la clase
    #lookup_url_kwarg = 'n' #le estoy diciendo a RetrieveApiView que busque por lo que en la url sea name


class DeleteDuck(DestroyAPIView):
    
    queryset = Duck.objects.all()
    serializer_class= allDucksSerializers
    permission_classes = [IsAuthenticated,IsAdminUser]


    


class UpdateDuck(UpdateAPIView):
    queryset = Duck.objects.all()
    serializer_class= allDucksSerializers

    

class CreateDuck(CreateAPIView):
    queryset = Duck.objects.all()
    serializer_class= CreateSerializers
    permission_classes = [IsAuthenticated,IsAdminUser]




class FiltratedList(ListAPIView):
    queryset = Duck.objects.all()
    serializer_class =allDucksSerializers
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ["id","nombre","segundo_nombre"]


"""
    def get_queryset(self ,*args, **kwargs):
        queryset_list = Duck.objects.all()
        query = self.request.GET.get("q")
        
        if query : 
            queryset_list=queryset_list.filter(
               Q(nombre__icontains = query)
              
            ).distinct()
            print(queryset_list)
        return queryset_list

"""


#------------pendiente------------
class UpdateDuckitem(UpdateAPIView):
    queryset=Duck.objects.all()
    lookup_field = 'field'
    serializer_class =  OnefieldSerializer
