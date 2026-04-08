#Zadanie 2
#Widzimy przed sobą nieoptymalną funkcję, która ma zwrócić potęge liczby w liście od 1 do n
#Zajmuje dużo pamięci i trzeba ją zmienić
#Zamień ją na generator

def nieoptymalna_funkcja(n):
    wynik = []
    for i in range(n):
        wynik.append(i ** 2)
    return wynik

def optymalny_generator(n):
    ...

n = 5

lista_wynikow = nieoptymalna_funkcja(n)
print(f"Zawartość: {lista_wynikow}")

gen = optymalny_generator(n)
for wartosc in gen:
    print(wartosc, end=" ")