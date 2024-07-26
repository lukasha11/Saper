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


def zlicz_sasiedztwo(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] == '*':
                try:
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
                except IndexError:
                    continue


def tworz_plansze(wymiar):
    plansza = []
    for i in range(wymiar):
        wiersz = []
        for j in range(wymiar):
            wiersz.append(Pole(0, 0, 0))
        plansza.append(wiersz)
    return plansza


class Pole:
    def __init__(self, czy_odkryta, wartosc, czy_bomba):
        self.czy_odkryta = czy_odkryta
        self.wartosc = wartosc
        self.czy_bomba = czy_bomba

    def dodaj_bombe(self):
        self.czy_bomba = 1


plansza = tworz_plansze(7)
wypelnij_bombami(plansza)
zlicz_sasiedztwo(plansza)
wyswietl_plansze(plansza)
