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
                tab[i][j].dodaj_bombe()
            licznik += 1


def zlicz_sasiedztwo(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j].czy_bomba == 1:
                try:
                    if not tab[i - 1][j - 1].czy_bomba:
                        tab[i - 1][j - 1].dodaj_wartosc()
                    if not tab[i - 1][j].czy_bomba:
                        tab[i - 1][j].dodaj_wartosc()
                    if not tab[i - 1][j + 1].czy_bomba:
                        tab[i - 1][j + 1].dodaj_wartosc()
                    if not tab[i][j - 1].czy_bomba:
                        tab[i][j - 1].dodaj_wartosc()
                    if not tab[i][j + 1].czy_bomba:
                        tab[i][j + 1].dodaj_wartosc()
                    if not tab[i + 1][j - 1].czy_bomba:
                        tab[i + 1][j - 1].dodaj_wartosc()
                    if not tab[i + 1][j].czy_bomba:
                        tab[i + 1][j].dodaj_wartosc()
                    if not tab[i + 1][j + 1].czy_bomba:
                        tab[i + 1][j + 1].dodaj_wartosc()
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


def pokaz_zera(x, y, tab, plansza):
    kierunki = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if tab[x][y]:
        return
    else:
        tab[x][y] = True
    if plansza[x][y].wartosc != -1:
        plansza[x][y].odkryj()

    if plansza[x][y].wartosc > 0:
        return

    for i, j in kierunki:
        if not(x + i >= len(tab) or y + j >= len(tab) or x + i < 0 or y + j < 0):
            pokaz_zera(x + i, y + j, tab, plansza)


class Pole:
    def __init__(self, czy_odkryta, wartosc, czy_bomba):
        self.czy_odkryta = czy_odkryta
        self.wartosc = wartosc
        self.czy_bomba = czy_bomba

    def dodaj_bombe(self):
        self.czy_bomba = 1
        self.wartosc = -1

    def dodaj_wartosc(self):
        self.wartosc += 1

    def odkryj(self):
        self.czy_odkryta = 1

    def __str__(self):
        if not self.czy_odkryta:
            return "[]"
        if self.czy_odkryta and self.czy_bomba:
            return "*"
        return str(self.wartosc)


def gra():
    plansza = tworz_plansze(7)
    wypelnij_bombami(plansza)
    zlicz_sasiedztwo(plansza)
    print("podaj wspolrzedne -> od 0,0 do 6,6")

    while (True):

        x = int(input("wsp x = "))
        y = int(input("wsp y = "))
        if plansza[x][y].wartosc == 0:
            tab = []
            for i in range(7):
                wiersz = []
                for j in range(7):
                    czy_byla = False
                    wiersz.append(czy_byla)
                tab.append(wiersz)
            pokaz_zera(x, y, tab, plansza)

        # if plansza[x][y].czy_odkryta:
        #     print("juz odkryta")
        #     continue
        plansza[x][y].odkryj()
        wyswietl_plansze(plansza)
        #cosik
        if plansza[x][y].czy_bomba:
            print("**BOOOOM**")
            break

gra()
