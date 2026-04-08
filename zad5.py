#Zadanie 5
#Zaimplementuj wydajny mechanizm przetwarzania strumieniowego (pipeline) przy użyciu generatorów.
#Mechanizm ten ma za zadanie oczyścić dane, przefiltrować parzyste liczby i je spotęgować nie wczytując je do pamięci RAM

def wczytaj_dane(n):
    for i in range(n):
        yield f"  Liczba: {i}"
#usun tekst
def oczysc_dane(it):
    ...
#przepuszczamy tylko parzyste
def filtruj_parzyste(it):
    ...

def potęguj(it):
    ...


# Tworzymy pipeline, łącząc generatory jeden w drugi
surowe = wczytaj_dane(1000000)
oczyszczone = oczysc_dane(surowe)
sparzyste = filtruj_parzyste(oczyszczone)
wynikowy_potok = potęguj(sparzyste)

for i in range(5):
    print(next(wynikowy_potok))