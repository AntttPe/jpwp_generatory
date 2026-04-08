# Zadanie 4
# Mamy iterator LicznikDoTrzech
# Zachowaj jego funkcję, ale zrób go generatorem lub wyrażeniem generatorowym


class LicznikDoTrzech:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n > 3:
            raise StopIteration
        return self.n


def licznik_do_trzech_generator():
    ...


for x in licznik_do_trzech_generator():
    print(x)