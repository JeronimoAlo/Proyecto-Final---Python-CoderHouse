import os
import json
import time

#La función "menu" se encarga de mostrar por pantalla una sería de items para que el usuario seleccione
#posteriormente.
def menu():
    os.system('cls')
    
    print("Menu:")
    print("1 - Cargar Usuarios a la BD.")
    print("2 - Iniciar sesión.")
    print("3 - Leer BD.")
    print("4 - Salir del programa.\n")

#La función "CargarUsuarios" se encarga de solicitar usuario y contraseña, para luego insertarlo dentro de
#un .json en formato diccionario.
def CargarUsuarios(Qusers, credenciales):
    if os.path.isfile("Usuarios.json"):
        with open("Usuarios.json", "r+") as BD:
            credenciales = json.load(BD)
	
            for i in range(Qusers):
	    
                usuario = input("Ingrese nombre de usuario: ")
                contraseña = input("Ingrese contraseña del usuario: ")
            
                credenciales[usuario] = contraseña
        
            BD.seek(0)
            json.dump(credenciales, BD)
            BD.close()

    else:
        with open("Usuarios.json", "w") as BD:
	
            for i in range(Qusers):
	    
                usuario = input("Ingrese nombre de usuario: ")
                contraseña = input("Ingrese contraseña del usuario: ")
            
                credenciales[usuario] = contraseña
        
            json.dump(credenciales, BD)
            BD.close()

#La función "LeerBD" se encarga de leer la base de datos en formato .json mediante un diccionario.
def LeerBD():
    if os.path.isfile("Usuarios.json"):
        with open("Usuarios.json", "r") as BD:
            datos = json.load(BD)
            BD.close()
        
            print(datos, "\n")

#La función "iniciar_sesion" se encarga de solicitar user y pass, para luego contrastar con la base de datos.
def iniciar_sesion():
    os.system('cls')

    int_user = input("Ingrese su nombre de usuario: ")
    int_pwd = input("Ingrese su contraseña: ")
    print("\n")

    with open("Usuarios.json", "r") as BD:
        datos = json.load(BD)

        if (int_user in datos) and (datos[int_user] == int_pwd):
            print("Inició sesión de forma correcta!\n")
        else:
            print("El usuario o contraseña es incorrecto.\n")

credenciales = {}

while True:
    menu()

    # Solicitamos una opción al usuario
    optMenu = int(input("Seleccione una opción del menu: "))
    print("\n")

    if optMenu == 1:
        Qusers = int(input("Cuantos usuarios desea cargar a la BD? "))
        CargarUsuarios(Qusers, credenciales)
        
        input("Usuarios cargados exitosamente.\nPulsa enter para volver al menu principal.")
        continue
    elif optMenu == 2:
        iniciar_sesion()

        print("Será redirigido al menú principal en 5 segundos")
        time.sleep(5)
        continue
    elif optMenu == 3:
        LeerBD()

        input("Pulsa enter para volver al menu principal.")
        continue
    elif optMenu == 4:
        print("Hasta luego!")
        break
    else:
        input("No has pulsado ninguna opción correcta.\nPulsa enter para volver al menu principal.")
        continue
