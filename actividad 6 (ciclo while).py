opcion = ""
while opcion != "C":
    print ("A. Saludar")
    print ("B. Mostrar el mensaje")
    print ("C. Salir")

    opcion = input("Ingrese un opción: ")
    print (opcion)
    if opcion == "A":
        print ("Bienvenido")
    elif opcion == "B":
        print ("Estamos aprendiendo el ciclo while")
    elif opcion == "C":
        print ("Salir")
    else:
        print ("Opción no válida")