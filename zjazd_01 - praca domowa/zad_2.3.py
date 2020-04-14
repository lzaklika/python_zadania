# ### Zadanie 2.3
# ​
# Napisz program, który odczytuje od użytkownika wiele liczb.
# ​
# Program powinien wyliczyć i na końcu wypisać następujące statystyki:
# ​
# - liczba podanych liczb (ile sztuk),
# - suma,
# - średnia,
# - minimum
# - maksimum
# ​
# NIE używaj funkcji wbudowanych!
ile_liczb = 0
suma = 0
max = None
min = None

while True:
    liczba = input("Podaj liczbę lub wciśnij ENTER, aby zakończyć i otrzymać wyniki: ")
    if liczba == "":
        srednia = suma / ile_liczb
        print(">>>ZAKOŃCZONO PODAWANIE LICZB<<<")
        print(f"Podano liczb: {ile_liczb}")
        print(f"Suma: {suma}")
        print(f"Średnia: {srednia}")
        print(f"Najniższa wartość: {min}")
        print(f"Najwyższa wartość: {max}")
    # if ile_liczb == 1:
    #     max = liczba
    #     min = liczba
    else:
        liczba = float(liczba)
        suma = suma + liczba
        ile_liczb += 1
        if max == None or max < liczba:
            max = liczba
        if min == None or min > liczba:
            min = liczba
