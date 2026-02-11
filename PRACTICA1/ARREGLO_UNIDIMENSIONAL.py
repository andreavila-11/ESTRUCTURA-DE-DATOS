x = [1, 2, 4, 4, 4, 5, 7, 9, 11, 11, 13, 14, 15, 16, 16]

y=[]

print("Arreglo original:", x)

for i in x:
    if i not in y:
        y.append(i)
        
print("Arreglo sin duplicados:", y)



