#Napisz program zamieniający miejscami w zadanej liście liczb element największy z najmniejszym

#na wejściu: [49, 50, 20, 40, 35, 10]
#na wyjsciu: [49, 10, 20, 40, 35, 50]


#         0   1   2   3   4   5
liczby = [49, 50, 20, 40, 35, 10]

# 1. Musimy znaleść indeks elementu o najwiekszej wartosci i i ndeksu o najmniejszej wartosci
# 2. Zamiana miejscami elementów z tych indeksów

# Wersja A
# 1. Używamy pętli for do znalezienia indeksów, atrz zadanie basics/zad_14
# 2. Zamieniamy wartości pod tymi indeksami

# Wersja B
# 1. Używając funkcji min(), max(), znajduje najmniejszą i największą wartość
# 2. Znajduję indeks tych elemntów w liście
# 3. Zamieniam te elementy miejcami
print(liczby)
max = liczby[0]
min = liczby[0]
for i, value in enumerate(liczby):
    if value > max:
        max_i = i
    elif value < min:
        min_i = i
temp = liczby[max_i]
liczby[max_i] = liczby[min_i]
liczby[min_i] = temp
print(liczby)
