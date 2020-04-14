# ### Zadanie 1.5 | Pole trójkąta (ok. 1 godz.)
# ​
# Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?),
# a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
# ​
# Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
# ​
# Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:
# ​
# ```
# import math
# ​
# x = math.sqrt(10)
# ```
#
import math
i = 0
liczby = []
min = None
max = None
while i < 3:
    bok = float(input("Podaj bok trójkąta"))
    liczby.insert(i, bok)
    i += 1
liczby.sort()
if liczby[0] + liczby [1] < liczby[2]:
    print("Z podanych długości boków nie można stworzyć trójkąta...")
else:
    p = (liczby[0] + liczby[1] + liczby[2]) / 2
    pole_trojkata = math.sqrt(p * (p - liczby[0]) * (p - liczby[1]) * (p - liczby[2]))
    print(f"Pole trójkąta jest równe: {pole_trojkata}")

