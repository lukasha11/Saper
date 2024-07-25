import random


def wyswietl_plansze(tab):
    for i in range(len(tab)):
        for j in tab[i]:
            print(j, end="\t")
        print()


def wypelnij_bombami(tab):
    licznik = 0
    losowane = random.sample(range(1, len(tab) * len(tab)), len(tab))
    for i in range(len(tab)):
        for j in range(len(tab)):
            if licznik in losowane:
                tab[i][j] = "*"
            licznik += 1

# def spr_sasiada(tab,i,j):
#     if tab[i - 1][j - 1]:
#
#         tab[i - 1][j]
#         tab[i - 1][j + 1]
#         tab[i][j - 1]
#         tab[i][j + 1]
#         tab[i + 1][j - 1]
#         tab[i + 1][j]
#         tab[i + 1][j + 1]
def zlicz_sasiedztwo(tab):
    for i in range(1, len(tab) - 1):
        for j in range(1, len(tab) - 1):
            if tab[i][j] == '*':
                if isinstance(tab[i - 1][j - 1], int):
                    tab[i - 1][j - 1] += 1
                if isinstance(tab[i - 1][j], int):
                    tab[i - 1][j] += 1
                if isinstance(tab[i - 1][j + 1], int):
                    tab[i - 1][j + 1] += 1
                if isinstance(tab[i][j - 1], int):
                    tab[i][j - 1] += 1
                if isinstance(tab[i][j + 1], int):
                    tab[i][j + 1] += 1
                if isinstance(tab[i + 1][j - 1], int):
                    tab[i + 1][j - 1] += 1
                if isinstance(tab[i + 1][j], int):
                    tab[i + 1][j] += 1
                if isinstance(tab[i + 1][j + 1], int):
                    tab[i + 1][j + 1] += 1


def tworz_plansze(wymiar):
    plansza = []
    for i in range(wymiar):
        wiersz = []
        for j in range(wymiar):
            wiersz.append(0)
        plansza.append(wiersz)
    return plansza


plansza = tworz_plansze(5)
wypelnij_bombami(plansza)
wyswietl_plansze(plansza)
zlicz_sasiedztwo(plansza)
print()
wyswietl_plansze(plansza)
