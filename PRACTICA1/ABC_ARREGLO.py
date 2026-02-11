cadena = "Parangaricutirimicuaro"

abecedario_min = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abecedario_may = [letra.upper() for letra in abecedario_min]

print("Letras minúsculas:")
for letra in abecedario_min:
    if cadena.find(letra) != -1:
        print (letra, ":", cadena.count(letra))

print("\nLetras mayúsculas:")
for letra in abecedario_may:
    if cadena.find(letra) != -1:
        print (letra, ":", cadena.count(letra))
        