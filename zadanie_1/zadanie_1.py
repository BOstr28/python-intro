import random

class Listy:
    def __init__(self, lista_1, lista_2):
        self.lista_1 = lista_1
        self.lista_2 = lista_2

    def polacz(self):
        return list(zip(self.lista_1, self.lista_2))
        # zip() łączy elementy z iterowanych obiektów w krotki. https://docs.python.org/3/library/functions.html#zip

    def losowy_element(self):
        try:
            return random.choice(self.lista_1)  # Losowy wybór z listy. https://docs.python.org/3/library/random.html
        except IndexError:
            print("Lista jest pusta") # IndexError zwraca błąd ponieważ jest próba dostępu do indeksu, który nie istnieje. https://docs.python.org/3/library/exceptions.html#IndexError
            return None
        
# Utworzone listy
lista_1 = [1, 2, 3]
lista_2 = ["apple", "orange", "banana"]

# Tworzenie obiektu
obiekt = Listy(lista_1, lista_2)

# Łączenie list
polaczone = obiekt.polacz()
print("Połączone listy: ", polaczone)

# Wybor losowego elementu
losowy = obiekt.losowy_element()
print("Losowy element z listy: ", losowy)

# GitHub: https://github.com/BOstr28/python-intro