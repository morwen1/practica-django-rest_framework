from django.urls import path
from django.contrib import admin 


from .views import (
    DuckList,
    DuckDetail,
    DuckDetail_pk,
    UpdateDuck,
    DeleteDuck,
    UpdateDuckitem,
    CreateDuck,
    FiltratedList,
)

urlpatterns = [ 
    path('list/' ,DuckList.as_view() , name='list'),
    path('nombre/<nombre>/' ,DuckDetail.as_view(),name ='detail'),
    path('pk/<int:pk>/' ,DuckDetail_pk.as_view(),name ='detail'),
    path('pk/<int:pk>/up' ,UpdateDuck.as_view(),name ='up'),
    path('pk/<int:pk>/del' ,DeleteDuck.as_view(),name ='del'),
    path('pk/<field>/one' ,UpdateDuckitem.as_view(),name ='one'),
    path('create/' ,CreateDuck.as_view() , name='list'),
    path('listfil/',FiltratedList.as_view(),name='filtrated'),



]