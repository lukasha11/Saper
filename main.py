import random

print("smth")

plansza = []
wymiar = 5

for i in range(wymiar):
    wiersz = []
    for j in range(wymiar):
        wiersz.append(0)
    plansza.append(wiersz)

for i in range(wymiar):
    print(plansza[i])

def wypelnij_bombami(tab, wymiar):
    licznik = 0
    losowane = random.sample(range(1, 26), 5)
    for i in range(wymiar):
        for j in range(wymiar):
            if licznik in losowane:
                tab[i][j] = "*"
            licznik += 1

wypelnij_bombami(plansza, wymiar)
for i in range(wymiar):
    print(plansza[i])