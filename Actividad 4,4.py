# %%
#  Nivel 1: Operaciones básicas
info= "Programación Para Todos"
print (info)
print(len(info))

# %%
# Nivel 2: Transformación de texto
print(str(info.upper()))
print(str(info.lower()))
print(str(info.title()))
print(str(info.capitalize()))

# %%
#  Nivel 3: Búsqueda y verificación
print(info.startswith("Programación"))
print(info.endswith("Todos"))
print(info.find("Para"))
print("Pyton"in info)

# %%
# Nivel 4: Manipulación
print(info.replace("Programación", "Python"))
print(info.split())
print("-".join(info))

# %% 
# Nivel 5: Índices 
print(info[0])
print(info[-1])
print(info[5])

# %%
#  Nivel 6: Aplicación simple
nombreCompleto= "Mishelle Pacheco"
print(f"Mi nombre completo es [nombreCompleto] ")
nombre=nombreCompleto.split()
print(nombre[0])