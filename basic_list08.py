# Készíts egy programot, melyben egy listát hozzol létre egész számokkal.
# Számolk ki a lista páros illetve páratlan elemeinek az összegét és írasd ki az eredményeket.
# Készíts két különböző megoldást!

egesz_szamok = list(range(11))
paros_osszeg = 0
paratlan_osszeg = 0
for x in egesz_szamok:
    if x % 2 ==0:
        paros_osszeg += x
    else:
        paratlan_osszeg += x
print(f"A páros számok összege: {paros_osszeg}")
print(f"A páratlan számok összege: {paratlan_osszeg}")


