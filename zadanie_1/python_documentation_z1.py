
#1 Opis funkcji wbudowanej - zip()

list_1 = [1,2,3]
list_2 = ["apple", "orange", "banana"]

zipped = list(zip(list_1, list_2))

print(zipped)
# zip() łączy elementy z iterowanych obiektów w krotki, 
# gdzie każda krotka zawiera elementy o tym samym indeksie z przekazanych iterowalnych obiektów.

# https://docs.python.org/3/library/functions.html#zip

#2 Opis modułu z biblioteki standardowej - random() 

import random

print(random.randint(1, 10)) # generuje losową liczbę z zakresu 1 - 10
print(random.choice(list_2))  # Losowy wybór z listy
# https://docs.python.org/3/library/random.html

#3 Opis wyjątku - ZeroDivisionError

try:
    result = 2/0
except ZeroDivisionError as a:
    print(f'Nie dziel przez 0 {a}')

# Własny wyjątek, ktory występuje gdy próbujemy podzielić liczbę przez 0

# https://docs.python.org/3/library/exceptions.html#ZeroDivisionError


