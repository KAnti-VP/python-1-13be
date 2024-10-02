erdemjegy = [1,2,3,4,5]
osztaly = ['9/ny', '9/a','10/b', '11/c', '12/b haladó', '1/13b', '2/14b']
adatok = ['Ákos', 'Dénes', 'Laci', 'Levente', 'Neli', 'Regi']

erdemjegy[0] = erdemjegy[2]
print(erdemjegy)

osztaly[1] = osztaly[2]
print(osztaly)

#adatok[-1] = adatok[2]
adatok[len(adatok)-1] = adatok[2]
print(adatok)
