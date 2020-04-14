# ### Zadanie 1.4 | Opłata hotelowa (ok 1,5 godz.)
# ​
# Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza, ile trzeba zapłacić. Zasady są takie:
# ​
# - nieletni (poniżej 18 roku życia) płacą 100 zł za noc
# - dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
# 	- 200 zł za noc, jeśli nocują jedną noc
# 	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
# 	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
# - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
# ​
# Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.

wiek = int(input("Podaj wiek: "))
while wiek < 0:
    ilosc_dni = int(input("Wiek nie może byc niższy od 0! Podaj wiek: "))
ilosc_dni = int(input("Podaj liczbe dni: "))
while ilosc_dni < 1:
    ilosc_dni = int(input("Liczba dni nie może być mniejsza od 1! Podaj liczbe dni: "))
cena_dziecko = 100
rabat = 0.1
if ilosc_dni == 1:
    cena_dorosly = 200
elif ilosc_dni < 5:
    cena_dorosly = 180
elif ilosc_dni >= 5:
    cena_dorosly = 150


if wiek < 18:
    wynik = ilosc_dni * cena_dziecko
elif wiek < 65:
    wynik = ilosc_dni * cena_dorosly
else:
    wynik = ilosc_dni * cena_dorosly * (1 - rabat)

print(f"Za pobyt w hotelu należy zapłacić {wynik} PLN")