from paquete1.modulo_cliente import Cliente
from paquete1.modulo_preEntrega1 import *

cliente1 = Cliente("Agustin", "agustin2023@gmail.com", 21, 2000)

print(cliente1) #__str__

cliente1.act_cuenta_corriente(1000) #Probamos función "act_cuenta_corriente".
cliente1.adquirir("Notebook i5") #Probamos función "adquirir".