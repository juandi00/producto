calificaciones = [4, 5, 3, 6, 7]
promedio = sum(calificaciones) / len(calificaciones)
if promedio >=5 :
    print("El alumno ha aprobado el curso")
else:
    print("El alumno ha reprobado el curso")

calificaciones = input("Ingrese las calificaciones separadas por espacios: ")
calificaciones = [int(calificacion) for calificacion in calificaciones.split()]

promedio = sum(calificaciones) / len(calificaciones)

if promedio >= 5:
    print("El alumno ha aprobado el curso")
else:
    print("El alumno ha reprobado el curso")