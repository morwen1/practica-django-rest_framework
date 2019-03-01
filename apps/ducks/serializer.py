from  .models import Duck
from rest_framework import serializers


class Duckserializer (serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Duck    
        fields =(
            'id',
            'nombre',
            'segundo_nombre',
            'edad',
        )