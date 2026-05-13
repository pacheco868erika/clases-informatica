#Ejercicios de listas 
notas = [8.5, 6.0, 9.0, 7.0, 5.5] 
suma = 0 
aprobaron = 0
reprobaron = 0
for calificacion in notas:
    suma = suma + calificacion
    if calificacion >= 7: 
     aprobaron + 1
    else:
       reprobaron + 1
promedio =  suma / len(notas)
