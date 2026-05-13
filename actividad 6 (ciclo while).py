
# %%
palabra = input ("Ingrese una palabra: ")
consonante = 0
vocales = 0
for letra in palabra.lower():
    if letra == "a" or letra == "e" or letra == "i" or letra =="o" or letra == "u":
        vocales = vocales + 1
    else:
        consonante= consonante + 1 
print (len(palabra))
print (f"Tiene este número de vocales: {vocales} y de consonantes {consonante}")
# %%

# for en un Set 
# %%
companias = {"Facebook", "Facebook",  "Google", "Apple", "Amazon"}
for compania in companias:
    print (compania)

# Break 
# %%
lista = [1, 2, 3, 4, 5]
numeros = int(input("Ingresa un número: "))
for numero in lista:
    if numero == numeros:
        print ("Número encontrado")
        break 
else:
    print ("Numero no encontrado")

# Continue 
# %%
cedula = input("Ingrese su número de cedula: ")
cedula_limpia = ""
for caracter in cedula:
    if caracter == "-" or caracter == " ":
        continue
    cedula_limpia = cedula_limpia + caracter
print (cedula_limpia)
# %%
