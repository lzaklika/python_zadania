# ### Zadanie 1.6 | Bilety (ok. 1 godz.)
# ​
# Założenia:
# 	- 0-6   - wiek przedszkolny - cena biletu: 0
# 	- 7-17  - wiek szkolny      - cena biletu: 2.28
# 	- 18-64 - wiek dorosły      - cena biletu: 3.80
# 	- +65   - wiek emerytalny   - cena biletu: 1.90
# ​
# Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
# ​
# Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.

wiek = int(input("Podaj wiek: "))
while wiek < 0:
    wiek = int(input("Wiek powinien być dodatni! Podaj wiek: "))
if wiek < 7:
    cena_biletu = 0
elif wiek < 18:
    cena_biletu = 2.28
elif wiek < 65:
    cena_biletu = 3.80
else:
    cena_biletu = 1.90
ilosc = int(input("Jaka ilość biletów ma zostać zakupiona?"))
wynik = cena_biletu * ilosc
print(f"Za bilety należy zapłacić {wynik} PLN")
