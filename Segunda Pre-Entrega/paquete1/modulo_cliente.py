class Cliente:

    def __init__(self, nombre, correo, edad, CC):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.CC = CC

    def __str__(self):
        return f"Se ha creado el cliente {self.nombre}"
    
    def act_cuenta_corriente(self, importe):
        self.CC += importe
        print("El nuevo importe de la CC de", self.nombre, "es de", self.CC)
    
    def adquirir(self, prod):
        print("El cliente", self.nombre, "adquirió un nuevo producto:", prod)


