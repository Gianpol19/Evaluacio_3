import random

class Vehiculo:

    def __init__(self, tipo, patente, marca, precio, multas, fecha_registro, nombre_dueno):

        self.tipo = tipo
        self.patente = patente
        self.marca = marca
        self.precio = precio 
        self.multas = multas 
        self.fecha_registro = fecha_registro 
        self.nombre_dueno = nombre_dueno 
        self.certificado_emision = random.randint(1500, 3500) 
        self.certificado_anotaciones = random.randint(1500, 3500) 
        self.certificado_multas = random.randint(1500, 3500) 

    def mostrar_info(self):

        print(f"Tipo: {self.tipo}")
        print(f"Patente: {self.patente}")
        print(f"Marca: {self.marca}")
        print(f"Precio: ${self.precio}")
        print(f"Multas: {self.multas}")
        print(f"Fecha de registro: {self.fecha_registro}")
        print(f"Nombre del dueño: {self.nombre_dueno}")

    def imprimir_certificado_emision(self):

        print(f"Certificado de emisión de contaminantes")
        print(f"Patente: {self.patente}")
        print(f"Nombre del dueño: {self.nombre_dueno}")
        print(f"Valor: ${self.certificado_emision}")

    def imprimir_certificado_anotaciones(self):

        print(f"Certificado de anotaciones vigentes")
        print(f"Patente: {self.patente}")
        print(f"Nombre del dueño: {self.nombre_dueno}")
        print(f"Valor: ${self.certificado_anotaciones}")

    def imprimir_certificado_multas(self):

        print(f"Certificado de multas")
        print(f"Patente: {self.patente}")
        print(f"Nombre del dueño: {self.nombre_dueno}")
        print(f"Valor: ${self.certificado_multas}")

def validar_patente(patente):

    if len(patente) == 6 and (patente[2] == "-" and patente[5] == "-") or (patente[4] == "-" and patente[6] == "-"):
        return True 
    else:
        return False 

def validar_marca(marca):

    if len(marca) >= 2 and len(marca) <= 15:

        return True
    else:

        return False 

def validar_precio(precio):

    if precio > 5000000:

        return True 

    else:

        return False 

vehiculos = []

opcion = 0

while opcion != 4:

    print("Menú de opciones")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1: 

        tipo = input("Ingrese el tipo de vehículo: ")
        patente = input("Ingrese la patente del vehículo: ")
        marca = input("Ingrese la marca del vehículo: ")
        precio = int(input("Ingrese el precio del vehículo: "))
        multas = [] 
        n_multas = int(input("Ingrese el número de multas del vehículo: ")) 
        for i in range(n_multas):

            monto = int(input(f"Ingrese el monto de la multa {i+1}: ")) 
            fecha = input(f"Ingrese la fecha de la multa {i+1}: ")
            multa = (monto, fecha) 
            multas.append(multa)
        fecha_registro = input("Ingrese la fecha de registro del vehículo (dd/mm/aa): ")
        nombre_dueno = input("Ingrese el nombre del dueño del vehículo: ")

        if validar_patente(patente) and validar_marca(marca) and validar_precio(precio):
            
            vehiculo = Vehiculo(tipo, patente, marca, precio, multas, fecha_registro, nombre_dueno)
            vehiculos.append(vehiculo)
            print("El vehículo ha sido registrado exitosamente.")

        else:

            print("Los datos ingresados no son válidos. Por favor, inténtelo nuevamente.")

    elif opcion == 2:

        patente = input("Ingrese la patente del vehículo a buscar: ")
        encontrado = False 

        for v in vehiculos:

            if v.patente == patente: 

                encontrado = True 
                v.mostrar_info() 
                break 
        if not encontrado: 

            print("No se encontró ningún vehículo con esa patente.")

    elif opcion == 3: 

        patente = input("Ingrese la patente del vehículo a imprimir los certificados: ")
        encontrado = False
        
        for v in vehiculos: 

            if v.patente == patente:

                encontrado = True 
                v.imprimir_certificado_emision()