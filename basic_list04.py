erdemjegy = [1,2,3,4,5]
osztaly = ['9/ny', '9/a','10/b', '11/c', '12/b haladó', '1/13b', '2/14b']
adatok = ['Ákos', 'Dénes', 'Laci', 'Levente', 'Neli', 'Regi']

print(erdemjegy)
del erdemjegy[0]
print(erdemjegy)

print(osztaly)
osztaly.pop(-1)
print(osztaly)

print(adatok)
adatok.remove(adatok[0])
print(adatok)

