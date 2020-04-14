# ### Zadanie 2.4 | Zgadnij liczbę z zakresu
# ​
# Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
# Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
# Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
# ​
# Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją i pełni w informatyce bardzo ważną rolę.
# Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024).
from random import randint

liczba = randint(0, 999)
i = 0

strzal = int(input("Zgadnij jaką liczbę wylosowano z zakresu 0-999! Wpisz liczbę: "))
i += 1
while strzal != liczba:
    if strzal > liczba:
        strzal = int(input(f"Wylosowana liczba jest mniejsza. Spróbuj jeszcze raz: "))
    else:
        strzal = int(input("Wylosowana liczba jest większa. Spróbuj jeszcze raz: "))
    i += 1
print(f"TAK! Wylosowana liczba, to {liczba}! Zgadłeś za {i} podejściem.")