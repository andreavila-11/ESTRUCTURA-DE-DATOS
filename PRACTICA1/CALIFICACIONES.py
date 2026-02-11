cal_alumnos = [8, 8, 7, 5, 10, 9, 9, 5, 6, 10]

suma= 0
n = len(cal_alumnos)

for cal in cal_alumnos:
    suma=suma+cal

promedio = suma/n

aprobados=0
reprobados=0

for cal_alumnos in cal_alumnos:
    if cal >= 7:
        aprobados +=1
    else:
        reprobados +=1
    
aprobados_porcentaje = (aprobados / n)*100
reprobados_porcentaje = (reprobados / n)*100

print ("Promedio del grupo:", promedio)
print ("Alumnos aprobados:", aprobados)
print ("Alumnos reprobados:", reprobados)
print ("Porcentaje aprobados:", aprobados_porcentaje )
print ("Porcentaje reprobados:", reprobados_porcentaje)
