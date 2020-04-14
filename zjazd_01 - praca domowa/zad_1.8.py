# ### Zadanie 1.8 | Kalkulator lat psich (ok. 0,5 godz.)
# ​
# Zakładamy, że 1 ludzki rok, to 5 lat psich.
# ​
# Za pomocą konsoli wczytaj imię i wiek psa.
# ​
# Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.
# ​
# Przykład:
# Podaj imię psa - Burek
# Podaj wiek psa - 3
# ​
# Gdyby Burek był człowiekiem, miałby 15 lat.

imie = str(input("Podaj imię psa: "))
wiek_psi = int(input(f"Ile {imie} ma lat?"))
wiek_ludzki = wiek_psi * 5
print(f"Gdyby {imie} był człowiekiem, miałby {wiek_ludzki} lat.")
