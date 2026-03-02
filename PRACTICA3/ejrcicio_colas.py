
def enque(lista, elemento):
    lista.append(elemento)

def deque(lista, lista2):
    enque(lista2, lista[0])
    lista.pop(0)

def retiros(lista, lista2):
    r = lista[0] - lista2[0]
    deque(lista, lista2)
    enque(lista, r)

def depositos(lista, lista2):
    r = lista[0] + lista2[0]
    deque(lista, lista2)
    enque(lista, r)

def peek(lista):
    return lista[0]

def is_empty(lista):
    return lista == []

def size(lista):
    return len(lista)

saldos   = [1000, 1000, 1000, 1000, 1000]
retiro   = [500]
deposito = [300]

print(saldos)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
print(saldos)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
print(saldos)