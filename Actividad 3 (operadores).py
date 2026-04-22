#Operadores
"""Nombre: Mishelle Pacheco
Fecha: 16/04/2026"""
# %%
# ariables
edad= 16 
estatura= 1.50

# %%
# base y altura de un triángulo 
base = float(input("Ingrese la base: ")) 
altura = float(input("Ingrese la altura: ")) 
area = 0.5 * base * altura 
print("Área:", area) 

# %%
#Lados de un triángulo y su perímetro
ladoA= float(input("Ingresa el lado A de un triángulo: "))
ladoB= float(input("Ingresa el lado B de un triángulo: "))
ladoC= float(input("Ingresa el lado C de un triángulo: "))
perimetro = ladoA + ladoB + ladoC
print("Perímetro: ", perimetro)

# %%
#la longitud y el ancho de un rectángulo
longitud= float(input("Ingresa la longitud de un rectángulo: "))
ancho= float(input("Ingresa la longitud de un ancho: ")) 
area= longitud * ancho 
perimetro = 2 * (longitud + ancho) 
print("Área:", area) 
print("Perímetro:", perimetro)

# %%
#área y la circunferencia de un círculo 
radio = float(input("Ingrese el radio: ")) 
pi = 3.14 
area = pi * radio * radio 
circunferencia = 2 * pi * radio 
print("Área:", area) 
print("Circunferencia:", circunferencia) 

# %%
#la pendiente y la distancia euclidiana entre los puntos
x1, y1 = 2, 2 
x2, y2 = 6, 10 
pendiente = (y2 - y1) / (x2 - x1) 
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5 
print("Pendiente:", pendiente) 
print("Distancia:", distancia) 

# %%
# Calcula el valor de y en la función:
x = -3 
y = x**2 + 6*x + 9 
print("y:", y) 

# %%
# Encuentra la longitud de las palabras y una comparación booleana (verdadero/falso)
print(len("python") == len("dragón")) 

# %%
# Usa el operador and para verificar si “on” está presente tanto en “python” como en “dragón”.  
print("on" in "python" and "on" in "dragón") 

# %%
#Usa el operador in para verificar si la palabra “jerga” está en la siguiente oración: 
oracion = "Espero que este curso no esté lleno de jerga" 
print("jerga" in oracion) 

# %%
#Verificar 'on' en python y dragon
print("on" in "python" and "on" in "dragon") 

# %%
# Longitud a float y string
valor = len("python") 
print(str(float(valor))) 

# %%
#División entera vs entero 
print(7 // 3 == int(2.7)) 

# %%
#Verifica si el tipo de dato de “10” es igual al tipo de dato de 10.   
print(type("10") == type(10)) 

# %%
# Verifica si int('9.8') es igual a 10.  
print(int(float("9.8")) == 10) 

# %%
# Calcula el pago total. 
horas = float(input("Ingrese horas: ")) 
tarifa = float(input("Ingrese tarifa por hora: ")) 
pago = horas * tarifa 
print("Pago:", pago) 

# %%
# Calcula la cantidad de segundos que ha vivido.
anios = int(input("Ingrese años: ")) 
segundos = anios * 365 * 24 * 60 * 60 
print("Segundos vividos:", segundos) 

# %%
#Escribe un programa en Python que muestre la siguiente tabla:  
print("1 1 1 1 1") 
print("2 1 2 4 8") 
print("3 1 3 9 27") 
print("4 1 4 16 64") 
print("5 1 5 25 125") 

