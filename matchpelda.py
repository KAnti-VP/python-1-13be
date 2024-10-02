nap_sorszama = int(input('Kérem a nap sorszámát: '))

match nap_sorszama:
    case 0 | 1 | 2 | 3 | 4: print("Munkanap")
    case 5 | 6: print("Hétvége")
    case _: print("Rossz napot adtál meg")