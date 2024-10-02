# darab = int(input('add meg az elemek számát.: '))
# lista = [None] * darab
# for i in range(darab, 0, -1):
#     lista[i-1] = int(input('kérek egy számot.: '))
# print(lista)

# darab = int(input('add meg az elemek számát.: '))
# lista = []
# for i in range(darab):
#     lista.append(int(input('kérek egy számot.: ')))
# lista.reverse()
# print(lista)

darab = int(input('add meg az elemek számát.: '))
lista = []
for i in range(darab):
    szam = int(input('kérek egy számot.: '))
    lista.insert(0, szam)
print(lista)