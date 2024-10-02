gyumolcsok = ['alma', 'Banan', 'cseresznye', 'Dinnye', 'Eper', 'fuge', 'granatalma']

# Írad ki az 1. és a 3. gyümölcsöt
print(gyumolcsok[0], gyumolcsok[2])
print(gyumolcsok[0:5])  # gyumolcsok[:5]
print(gyumolcsok[-5:])
print(gyumolcsok[1:6])

# Változtas meg az elsőt 'körte' értékre
gyumolcsok[0] = 'korte'
print(gyumolcsok)

# Ciklussal való bejárás
for x in gyumolcsok:
    print(x, end=' - ')
print()

for i in range(len(gyumolcsok) - 1):
    print(gyumolcsok[i], end=' * ')
print(gyumolcsok[-1])

gyumi = 'fuge'
if gyumi in gyumolcsok:
    print(f'A(z) {gyumi} benne van a gyumolcsok listában.')
else:
    print(f'A(z) {gyumi} nincs benne a gyumolcsok listában.')

gyumolcsok[1:3] = ['ananasz', 'mango', 'kiwi']
print(gyumolcsok)

gyumolcsok[-3:-1] = ['szilva']
print(gyumolcsok)

gyumolcsok.insert(0, 'licsi')
print(gyumolcsok)

zoldsegek = ['repa', 'retek', 'mogyorohagyma']

zoldsegek.append('kaposzta')
print(zoldsegek)

#zoldsegek.extend(gyumolcsok)
salata = zoldsegek + gyumolcsok
print(salata)
print()
print(zoldsegek)
zoldsegek[-2:] = []
print(zoldsegek)

zoldsegek.remove('retek')
print(zoldsegek)

szamaim = [2, 4, 6, 8, 12]
szamaim.remove(4)
print(szamaim)

szamaim.pop(0)
szamaim.pop()
print(szamaim)

salata.clear()
print(salata)

# for i in range(len(gyumolcsok)):
#     gyumolcsok[i] = gyumolcsok[i].capitalize()
# print(gyumolcsok)

összeg = 0
for x in gyumolcsok:
    összeg += len(x)
print(f'A lista elemeinek össz hossza: {összeg}')

newlist = [x for x in range(10)]

print(newlist)

lst = list(range(0,10, 2))
print(lst)

szamok = [23, 3, 50, 34, 89, 11, 1, 28, 70, 3, 23, 3]
#szamok.sort()
#szamok.sort(reverse=True)
#szamok.reverse()
szamok.sort(key=lambda x: abs(25 - x))
print(szamok)

nevek = ['Alma', 'bimbo', 'cica', 'David', 'Eperke', 'frici']
# nevek.sort(key=lambda x: x.lower())
nevek.sort(key=str.lower)
print(nevek)

lst1 = [1, 3, 5, 7]
#lst2 = lst1.copy()
#lst2 = lst1[:]
lst2 = list(lst1)
print(lst1, lst2)
lst1.append(9)
print(lst1, lst2)

print(szamok.count(3))
print(szamok.count(23))
print(szamok.count(70))
print(nevek.count('Eperke'))
print('-'*20)
print(szamok)
print(szamok.index(3))
print(szamok.index(23))
print(szamok.index(70))
print(nevek.index('Eperke'))

print('-'*20)
txt = 'Képzeld, nyertem a lottón,... kettesem volt.'
# szavak = txt.split()
# szavak = txt.split('.')
szavak = list(txt)
print(szavak)

fruits = ' * '.join(gyumolcsok)
print(fruits)

print(''.join(szavak))
print(nevek)
nevek_rendezve = sorted(nevek, reverse=True)
print(nevek_rendezve)
print(nevek)