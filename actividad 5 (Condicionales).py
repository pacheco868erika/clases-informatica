A = 3
if A>0:
  print(f"{A} es positivo")
else:
  print(f"{A} es negativo")
print("Gracias por usar el programa")

#%%
#=Ejercicio
nota=int(input("Ingrese su calificación "))
if nota >= 90:
  print("A")
else:
  if nota >=80:
    print("B")
  else:
    if nota >= 70:
      print("C")
    else:
      if nota < 70:
        print("D")

# %%
# Ejercicio de if anillados
numero= float(input("Ingrese un numero"))
if numero== 0:
  print("El numero es 0")
else:
  if numero>0:
    if (numero % 2==0):
      print("El numero es par y positivo")
    else:
      print("El numero es impar y positivo")
  else:
    if (numero % 2==0):
      print("El numero es par y negavitivo")
    else:
      print("El numero es impar y negativo")

# %%
numero= float(input("Ingrese un numero"))
if numero > 0 and numero % 2==0:
  print("El numero es par y positivo")
elif numero > 0 and numero % 2==1:
  print("El numero es impar y positivo")
elif numero < 0 and numero % 2==0:
  print("El numero es par y negativo")
elif numero < 0 and numero % 2==1:
  print("El numero es impar y negavito")
else:
  print("El numero es 0")

# %%
# Short hand
numero= float(input("Ingrese un numero"))
print("Numero es positivo") if numero > 0 else print ("Numero es negativo")
print("Numero es par") if numero % 2 ==0 else print ("Numero es impar")
print("Numero es 0") if numero == 0 else print ("Gracias por usar")