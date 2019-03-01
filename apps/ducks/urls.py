from django.conf.urls import url 
from .views import Ducklist

urlpatterns = [
    url('patos/',Ducklist.as_view(),name='ducks')
]