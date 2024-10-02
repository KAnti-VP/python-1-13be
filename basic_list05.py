lista = [21, 32, 13, 44, 75] 
szam = int(input("Mondj egy számot:"))
melyiket = int(input("Melyik számra módosítsa?"))

index = melyiket - 1

if index >= len(lista) or index < 0:
    print("Nincs ilyen elem")
else:
    lista[index] = szam 
print(lista)

lista.pop()
print(lista)

print(len(lista))

for x in lista:
    print(x)
    