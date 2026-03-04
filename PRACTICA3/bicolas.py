# ── Operaciones de bicola con lista ───────────────────────────────
def enqueue_rear(bicola: list, elemento):
    bicola.append(elemento)

def enqueue_front(bicola: list, elemento):
    bicola.insert(0, elemento)

def peek_front(bicola: list):
    return bicola[0]

def peek_rear(bicola: list):
    return bicola[-1]

def is_empty(bicola: list) -> bool:
    return bicola == []

def size(bicola: list) -> int:
    return len(bicola)

# ── Operaciones bancarias ──────────────────────────────────────────
def retiros(saldos: list, montos: list) -> None:
    saldo = peek_front(saldos)
    monto = peek_front(montos)      # lee el primer monto
    enqueue_rear(saldos, saldo - monto)
    saldos.pop(0)
    montos.pop(0)                   # elimina el monto usado, avanza al siguiente

def depositos(saldos: list, montos: list) -> None:
    saldo = peek_front(saldos)
    monto = peek_front(montos)
    enqueue_rear(saldos, saldo + monto)
    saldos.pop(0)
    montos.pop(0)

# ── Datos ──────────────────────────────────────────────────────────
saldos   = [1000, 1000, 1000, 1000, 1000]
retiro   = [500, 400, 300, 200, 100]   # ← 5 valores distintos
deposito = [300, 300, 300, 300, 300]   # ← 5 valores iguales

print("Saldos iniciales:", saldos)

for _ in range(5):
    retiros(saldos, retiro)

print("Tras 5 retiros:  ", saldos)

for _ in range(5):
    depositos(saldos, deposito)

print("Tras 5 depósitos:", saldos)
