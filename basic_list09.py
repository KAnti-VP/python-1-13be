#Készíts programot, melyben megadsz egy listát.
# Fordítsd meg a lista elemeinek a sorrendjét és írasd ki a listát!
# Készíts több megoldást!

lista = [1, "alma", 2, 13, 3.14, "bab"]
# lista.reverse()
# lista = lista[::-1]
lista = list(reversed(lista))

print(lista)