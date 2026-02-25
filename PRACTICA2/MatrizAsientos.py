Asientos = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

def reservar(i, j):
    fila = i - 1
    columna = j - 1
    if Asientos[fila][columna] == 1:
        print(f"RECHAZO: ocupado ({i},{j})")
    else:
        Asientos[fila][columna] = 1
        print(f"OK: reservado ({i},{j})")

def liberar(i, j):
    fila = i - 1
    columna = j - 1
    if Asientos[fila][columna] == 0:
        print(f"RECHAZO: ya libre ({i},{j})")
    else:
        Asientos[fila][columna] = 0
        print(f"OK: liberado ({i},{j})")

def consultar(i, j):
    fila = i - 1
    columna = j - 1
    if Asientos[fila][columna] == 0:
        print(f"Estado = libre ({i},{j})")
    else:
        print(f"Estado = reservado ({i},{j})")   

reservar(1, 1)
reservar(1, 2)
reservar(1, 1)
consultar(1, 1)
liberar(1, 1)
liberar(1, 1)
reservar(3, 4)
reservar(6, 6)
consultar(6, 6)
reservar(2, 5)

total_reservados = 0
fila_max = 0
max_reservados = 0

for i in range(len(Asientos[0])):
    reservados_fila = 0
    for j in range(len(Asientos[0])):
        if Asientos[i][j] == 1:
            total_reservados += 1
            reservados_fila += 1
    if reservados_fila > max_reservados:
        max_reservados = reservados_fila
        fila_max = i + 1

print(f"Total reservados = {total_reservados}")
print(f"Fila con más reservados = {fila_max}")
       
    