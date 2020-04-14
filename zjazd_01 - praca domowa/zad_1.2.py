# ### Zadanie 1.2 | Buty do szewca (ok. 1 godz.)
# ​
# Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1, wtorek to dzień 2 itp.).
# Ma też podać, ile dni będzie trwała naprawa.
# ​
# Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
# Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.

dni_tygodnia = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]

naprawa_start = int(input("W jaki dzień tygodnia oddałeś buty? (poniedziałek to dzień 1, wtorek dzień 2, ... niedziela to dzień 7)"))
if naprawa_start > 7 or naprawa_start < 1:
    naprawa_start = int(input("Podany numer nie odpowiada żadnemu dniowi tygodnia. Podaj numer z zakresu <1, 7>!"))

naprawa_czas = int(input("Ile dni będzie trwała naprawa?"))
if naprawa_czas < 0:
    naprawa_czas = int(input("Ten szewc nie umie podróżować w czasie! Podaj dodatnią liczbę dni"))

naprawa_koniec = (naprawa_start + naprawa_czas) % 7 - 1
print(f"Buty będą gotowe za {naprawa_czas} dni. Dzień odbioru: {dni_tygodnia[naprawa_koniec]}")


