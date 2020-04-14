# ### Zadanie 2.1 | Zagadka matematyczna
# ​
# Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
# Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
# Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
# Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
from random import randint

i = randint(0, 99)
j = randint(0, 99)
suma = i + j
suma_uzytkownika = int(input(f"Wylosowane liczby, to: {i} i {j}. Jaka jest ich suma?"))
while suma_uzytkownika != suma:
    suma_uzytkownika = int(input(f"Podany wynik jest nieprawidłowy! Podaj sumę liczb {i} i {j}:"))
if suma_uzytkownika == suma:
    print(f"Dobrze!")

