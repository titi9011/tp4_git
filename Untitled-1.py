def test(nombre):
    return nombre + 1

def boucle(nombre):
    ouverte = True
    while ouverte:
        nombre = test(nombre)
        print(nombre)
        if nombre == 10:
            ouverte = False

boucle(2)