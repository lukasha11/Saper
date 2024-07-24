import random

def wyswietl_plansze(tab):
    for i in range(wymiar):
        print(tab[i])

def wypelnij_bombami(tab, wymiar):
    licznik = 0
    losowane = random.sample(range(1, wymiar*wymiar), wymiar)
    for i in range(wymiar):
        for j in range(wymiar):
            if licznik in losowane:
                tab[i][j] = "*"
            licznik += 1

def zlicz_sasiedztwo(tab):
    for i in range(1, wymiar - 1):
        for j in range(1, wymiar - 1):
            if tab[i][j] == '*':



plansza = []
wymiar = 5
for i in range(wymiar):
    wiersz = []
    for j in range(wymiar):
        wiersz.append(0)
    plansza.append(wiersz)


wypelnij_bombami(plansza, wymiar)

wyswietl_plansze(plansza)
