nombre = input("Nombre: ")
clases_programadas = int(input("Clases programadas: "))
clases_asistidas = int(input("Clases asistidas: "))
nota = float(input("Calificación final: "))

asistencia = (clases_asistidas / clases_programadas) * 100

if asistencia >= 80:
    if nota >= 51:
        condicion = "Aprobado"
    else:
        condicion = "Reprobado por nota"
else:
    condicion = "Reprobado por asistencia"

print("Porcentaje de asistencia:", asistencia)
print("Condición:", condicion)