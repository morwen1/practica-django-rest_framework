from rest_framework.serializers import ModelSerializer
from apps.ducks.models import Duck

class CreateSerializers(ModelSerializer):
    class Meta():
        model=Duck
        fields = [
            'nombre',
            'segundo_nombre',
            'mail',
            'edad',
            ]
        


class ListDucksSerializers(ModelSerializer):
    class Meta ():
        model = Duck
        fields = [
            'id',
            'nombre',
            'mail',
        ]



class allDucksSerializers(ModelSerializer):
    class Meta ():
        model = Duck
        fields = [
            'id',
            'nombre',
            'segundo_nombre',
            'mail',
        ]
            
#---------------pendiente debe ser un serializer custom que devuelva los fields que yo quiera -------------
 
class OnefieldSerializer(ModelSerializer):
    class Meta():
        
        model = Duck
        fileds = ["nombre"]
        """
            model_fields = [
            'nombre',
            'segundo_nombre',
            'mail',
            'edad',
            ]
            for i in model_fields:
                if i == item:
                  
                    fields = list(i)
                    break
        
        """
        
                
                

    


   