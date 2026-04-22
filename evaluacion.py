# %%
# ===== PARTE A =====
# Respuesta 1: 
# a) Indica el tipo de dato de cada variable. 
# El tipo de dato de nombre es str
# El tipo de dato de edad es int
# El tipo de dato de promedio es float 
# El tipo de dato de cursos es list

# b) Escribe qué mostraría el programa en pantalla. 
# Lo que mostraría el programa es el tipo de variable que es nombre, edad, promedio y cursos.
# Además va a mostrar  cuantas letras tienen la variable nombre.

#c) Explica qué hace len(nombre). 
# El len en nombre, nos dice cuantas letras tiene el dato que está dentro de la variable nombre.


# Respuesta 2:
# a) ¿Qué diferencia hay entre print() e input()? 
# Print solo imprimi datos especificos que le indicamos en el código para que se muestre en la pantalla, mientras que input es para que el usuario ingrese datos desde el teclado.

# b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo? 
# Poruqe un sato guardaddo en inpu se considera ua cadena de texto, no valores númericos

# c) Explica la diferencia entre /, // y %. 
# La diferencia es que mod % te da el residuo de la división, mientras que  div // solo te da el resultado entero (solo lo que este antes de la coma). Por último, / te da el resultado de la divición normal en datos float

# d) Escribe una instrucción que permita comprobar la versión de Python que se está usando. 
# $ python --version   (Lo haces en Git Bash )

# e) Escribe una instrucción que permita consultar las palabras reservadas de Python. 
#la instrucción es help("keywords")

# %%
# ===== PARTE B ===== 
# Código corregido 
ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * largo
costo = area * precio
print("Área total: " + str(area))
print("Costo estimado: " + str(costo))

# a) ¿Cuáles eran los errores principales? 
# Los errores principales es que las variables del ancho, largo y precio estaban guardadas como datos str, debido a input, por lo cual no sirven para realizar operaiones matemáticas.
# Además cuando se quería mostrar el resultado el código lo mostraba como datos float, por lo cual se debe cambiar a datos str para que se muestren como cadena de texto.

# b) ¿Por qué tu corrección sí permite obtener resultados válidos? 
# Porque transforma los datos de str a float, lo que permite realizar las operaciones matemáticas. Tambien al final transforma los datos float a str para unir la informació sin errores en la respuesta final 

# Construcción breve
frase= "Tecnología para todos"
print(frase.upper)
print(len(frase))
print("Python" in frase)
print(frase. replace("Tecnología", "Programación"))
print(frase.split())












