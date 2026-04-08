#Zadanie 1
#Sprawdź ile miejsca w pamięci zajmuje lista vs ile miejsca zajmuje generator
#wykorzystaj do tego funkcję sys.getsizeof


import sys

# Podejście zachłanne (Lista)
lista = [i for i in range(1000000)]

# Generator
generator = (i for i in range(1000000))

# Miejsce zajęte przez listę
print(...)

# Miejsce zajęte przez generator
print(...)