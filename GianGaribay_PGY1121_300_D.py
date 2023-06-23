vehiculos = []
patentes = []
marcas = []
precios = []
multas = []
fechas_registro = []
nombres_dueño = []

def grabar_vehiculo():

    tipo = input ("Ingrese el tipo de vehiculo: ")
    patente = input ("Ingrese la patente del vehiculo: ")
    while patente in patentes:
        print("La patente ya existe. Ingrese otra.")
        patente = input ("Ingrese el tipo de vehiculo: ")

    marca = input ("Ingrese la marca del vehiculo: ")
    while len(marca) < 2 or len(marca) > 15:
        print ("La marca debe tener entre 2 y 15 caracteres.")
        marca = input ("Ingrese la marca del vehiculo: ")
    
    precio = int(input("Ingrese el precio del vehiculo: "))
    while precio <= 5000000:
        print ("El precio debe ser mayor a $5.000.000.")
        precio = int(input("Ingrese el precio del vehiculo: "))
    
    multa_monto = int(input("Ingrese el monto de la multa: "))
    multa_fecha = input("Ingrese la fecha de la multa (dd/mm/aa): ")
    fecha_registro = input("Ingrese la fecha del registro del vehiculo (dd/mm/aa): ")
    nombre_dueño = input ("Ingrese el nombre del dueño del vehiculo: ")

    vehiculos.append(tipo)
    patentes.append(patente)
    marcas.append(marca)
    precios.append(precio)
    multas.append(multa_monto, multa_fecha)
    fechas_registro.append(fecha_registro)
    nombres_dueño.append(nombre_dueño)

def buscar_vehiculo():
    patente = input("ingrese la patente del vehiculo: ")
    if patente in patentes:
        indice = patentes.index(patente)
        print("Tipo:", vehiculos[indice])
        print("Patente:", patentes[indice])
        print("Marca:", marcas[indice])
        print("precio:", precios[indice])
        print("Multas:", multas[indice])
        print("Fecha de registro:", fechas_registro[indice])
        print("Dueño:", nombres_dueño[indice])
    else:
        print("La patente no existe.")

import random

def imprimir_certificados():
    patente = input("ingrese la patente del vehiculo: ")
    if patente in patentes:
        indice = patentes.index(patente)
        print("Certificado de emision de contaminantes")
        print("Patente:", patentes[indice])
        print("Dueño:", nombres_dueño[indice])
        print("Valor:", random.randint(1500, 3500))
        print()
        print("Certificado de anotaciones vigentes")
        print("Patente:", patentes[indice])
        print("Dueño:", nombres_dueño[indice])
        print("Valor:", random.randint(1500, 3500))
        print()
        print("Certificado de multas")
        print("Patente:", patentes[indice])
        print("Dueño:", nombres_dueño[indice])
        print("Valor:", random.randint(1500, 3500))
    else:
        print("La patente no existe.")

def validar_patente(patente):
    if patente in patentes:
        return False
    else:
        return True

def validar_marca(marca):

    if len(marca) < 2 or len(marca) > 15:
        return False
    else:
        return True

def validar_precio(precio):

    if precio <= 5000000:
        return False
    else:
        return True