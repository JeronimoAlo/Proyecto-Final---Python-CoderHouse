from django.urls import path
from AppPreEntreg3 import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),  
    path('remeras', views.remeras, name="Remeras"),
    path('buzos', views.buzos, name="Buzos"),
    path('pantalones', views.pantalones, name="Pantalones"),
    path('remerasForm', views.remerasForm, name="remerasForm"),
    path('buzosForm', views.buzosForm, name="buzosForm"),
    path('pantalonesForm', views.pantalonesForm, name="pantalonesForm"),
    path('busquedaRemera',views.busquedaRemera,name="BusquedaRemera"),
    path('buscarRem/',views.buscarRem),
    path('busquedaBuzo',views.busquedaBuzo,name="BusquedaBuzo"),
    path('buscarBuzo/',views.buscarBuzo),
    path('busquedaPantalon',views.busquedaPantalon,name="BusquedaPantalon"),
    path('buscarPant/',views.buscarPant),
]