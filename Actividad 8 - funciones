def generate_full_name():
    nombre= "Mishelle"
    apellido= "Pacheco"
    space= " "
    nombre_completo = nombre + space + apellido
    print (nombre_completo)
generate_full_name()
generate_full_name()
generate_full_name()

# eJEMPLO 2
def instrucciones ():
    print("===INSTRUCCIONES DEL PROGRAMA===")
    print("1. Ingresa tu nombre")
    print("2. Ingresa tu edad")
    print("3. El programa mostrará un mensaje personalizado")
    
def despedida():
    print("Gracias por usar el programa")
    
print("===SITEMA DE REGISTRO===")
opcion= input("Deseas ver las instrucciones? si/no ")
if opcion == "si":
    instrucciones()
nombre= input("Ingrese su nombre: ")
edad= input("Ingrese su edad: ")
print(f"Hola {nombre} tienes {edad} años")
despedida() 

# Ejemplo 3
def saludar (nombre): 

    print (f"hola {nombre}") 

saludar("Mishelle") 

# DEBER
def mostrar_estudiante(nombre, curso):
    print ("===DATOS DEL ESTUDIANTE===")
    print (f"Nombre: {nombre}")
    print (f"Curso: {curso}")
    print("-------------------")
    
def mensaje_final():
    print("Fin del programa")
    
estudiantes = int(input("¿Cuántos estudiantes desea ingresar?: "))
contador = 1
while contador <= estudiantes:
    print("Registro del estudiante", contador)
    nombre = input("Ingrese el nombre del estudiante: ")
    curso = input("Ingrese el curso del estudiante: ")
    mostrar_estudiante(nombre, curso)
    contador += 1
mensaje_final()

def calcular_promedio (nombre, apellido, nota1, nota2, nota3):
    print (f"Tu nombre es {nombre}, y tu apellido es {apellido}")
    promedio = (nota1 + nota2 + nota3) / 3
    print (f"Tu promedio es: {promedio}")
    
nombre = input ("Ingresa tu nombre : ")
apellido = input ("Ingresa tu apellido: ")
nota1 = float(input("Ingrese la primera nota: ")) 
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
calcular_promedio (nombre, apellido, nota1, nota2, nota3)

# segundo ejercicio 
def obtener_mensaje ():
    mensaje = "Bienenido al sistema"
    return mensaje 

def generar_nombre_completo():
    nombre = input ("Ingresa tu nombre: ")
    apellido = input ("Ingresa tu apellido: ")
    nombre_completo= nombre + " " + apellido 
    return nombre_completo 
    

print (obtener_mensaje())
print (generar_nombre_completo())

# Ejercicio de puntos 
def calcular_total_producto(precio, cantidad):
    return precio * cantidad
print("=== SISTEMA DE COMPRA ===")
subtotal = 0
for i in range(1, 4):
    print(f"\nProducto {i}")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        print("Precio no válido. Debe ser mayor que 0.")
        precio = float(input("Ingrese nuevamente el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    while cantidad <= 0:
        print("Cantidad no válida. Debe ser mayor que 0.")
        cantidad = int(input("Ingrese nuevamente la cantidad comprada: "))
    total_producto = calcular_total_producto(precio, cantidad)
    subtotal += total_producto
    print(f"Producto registrado: {nombre}")
    print(f"Total del producto: ${total_producto}")
iva = subtotal * 0.15
total_pagar = subtotal + iva
print("=== RESUMEN DE COMPRA ===")
print(f"Subtotal: ${subtotal}")
print(f"IVA (15%): ${iva}")
print(f"Total a pagar: ${total_pagar}")

# Ejercicio de practica 1 
def centimetros (metros):
    resultado = metros * 100
    return resultado
def milimetros (metros): 
    resultado = metros * 1000
    return resultado
def kilometros (metros):
    resultado = metros / 1000
    return resultado
def pulgadas (metros):
    resultado = metros * 39.3701 
    return resultado 

metros = int(input ("Ingresa una cantidad en metros: "))
print ("===MENÚ===")
print ("1.Centímetros") 
print ("2. Milímetros")
print ("3.Kilómetros")
print ("4.Pulgadas ")
print ("5.Salir del programa")
numero = int(input ("Ingrese que transformación quiere hacer: "))
while True:
    if numero ==1:
        print (f"El resultado en centimetros es {centimetros (metros)}")
        break
    elif numero ==2: 
        print (f"El resultado en milimetros es {milimetros (metros)}")
        break
    elif numero ==3:
        print (f"El resultado en kilometros {kilometros (metros)}")
        break
    elif numero ==4:
        print (f"El resultado en pulgadas es {pulgadas (metros)}")
        break
    elif numero == 5: 
        print ("Saliendo del programa")
        break
    else:
        print ("Opción inválida")
    
