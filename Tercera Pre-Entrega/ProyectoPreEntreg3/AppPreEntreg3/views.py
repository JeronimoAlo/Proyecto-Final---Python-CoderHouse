from django.shortcuts import render
from django.http import HttpResponse
from AppPreEntreg3.models import ProdRemera, ProdBuzo, ProdPantalon
from AppPreEntreg3.forms import RemerasForm, BuzosForm, PantalonesForm

# Create your views here.

def inicio(request):
    return render(request, 'AppPreEntreg3/inicio.html')

def remeras(request):
    remeras = ProdRemera.objects.all() # trae todas las remeras.
    contexto= {"remeras": remeras}
    return render(request, 'AppPreEntreg3/remeras.html', contexto)

def buzos(request):
    buzos = ProdBuzo.objects.all() # trae todos los buzos.
    contexto= {"buzos": buzos}
    return render(request, 'AppPreEntreg3/buzos.html', contexto)

def pantalones(request):
    pantalones = ProdPantalon.objects.all() # trae todos los pantalones.
    contexto= {"pantalones": pantalones}
    return render(request, 'AppPreEntreg3/pantalones.html', contexto)

def busquedaRemera(request):
     return render(request,'AppPreEntreg3/busquedaRemera.html')

def busquedaBuzo(request):
     return render(request,'AppPreEntreg3/busquedaBuzo.html')

def busquedaPantalon(request):
     return render(request,'AppPreEntreg3/busquedaPantalon.html')

def remerasForm(request):
    if request.method == "POST":
        miFormulario = RemerasForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            remeras = ProdRemera(int(informacion['id']),str(informacion['nombre']),str(informacion['tamaño']), 
                                 informacion['color'], float(informacion['precio']), int(informacion['stock']))
            remeras.save()
            return render(request, "AppPreEntreg3/remeras.html")
    else:
        miFormulario = RemerasForm() #Formulario vacío.
             
    return render(request, "AppPreEntreg3/remerasForm.html", {"miFormulario": miFormulario})

def buzosForm(request):
    if request.method == "POST":
        miFormulario = BuzosForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            buzos = ProdBuzo(int(informacion['id']),str(informacion['nombre']),str(informacion['tamaño']), 
                                 informacion['color'], float(informacion['precio']), int(informacion['stock']))
            buzos.save()
            return render(request, "AppPreEntreg3/buzos.html")
    else:
        miFormulario = BuzosForm() #Formulario vacío.
             
    return render(request, "AppPreEntreg3/buzosForm.html", {"miFormulario": miFormulario})

def pantalonesForm(request):
    if request.method == "POST":
        miFormulario = PantalonesForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            pantalones = ProdPantalon(int(informacion['id']),str(informacion['nombre']),str(informacion['tamaño']), 
                                 informacion['color'], informacion['diseño'], float(informacion['precio']), int(informacion['stock']))
            pantalones.save()
            return render(request, "AppPreEntreg3/pantalones.html")
    else:
        miFormulario = PantalonesForm() #Formulario vacío.
             
    return render(request, "AppPreEntreg3/pantalonesForm.html", {"miFormulario": miFormulario})

def buscarRem(request):
    if request.GET['remera']:
        remera = request.GET['remera']
        remeras = ProdRemera.objects.filter(nombre__icontains=remera)

        return render(request,'AppPreEntreg3/resultadosRemeras.html', {"remeras":remeras, "remera": remera })
    else:
        respuesta= "No enviaste datos"

    return render(request,"AppPreEntreg3/inicio.html",{"respuesta":respuesta})

def buscarBuzo(request):
    if request.GET['buzo']:
        buzo = request.GET['buzo']
        buzos = ProdBuzo.objects.filter(nombre__icontains=buzo)

        return render(request,'AppPreEntreg3/resultadosBuzos.html', {"buzos":buzos, "buzo": buzo })
    else:
        respuesta= "No enviaste datos"

    return render(request,"AppPreEntreg3/inicio.html",{"respuesta":respuesta})

def buscarPant(request):
    if request.GET['pantalon']:
        pantalon = request.GET['pantalon']
        pantalones = ProdPantalon.objects.filter(nombre__icontains=pantalon)

        return render(request,'AppPreEntreg3/resultadosPantalones.html', {"pantalones":pantalones, "pantalon": pantalon })
    else:
        respuesta= "No enviaste datos"

    return render(request,"AppPreEntreg3/inicio.html",{"respuesta":respuesta})
