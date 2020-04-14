# Napisz program wypisujacy na konsolę tabliczkę mnożenia
# dla liczb od 0 do 9 w postaci tabelki

# DO DOMU: przerobić ten program tak, żeby wyświetlał tabliczkę mnozenia tak, żeby wyświetlał od 0 do 100
print("     ", end=" ")
for i in range (0, 101):
    print(f"{i:5}", end=" ")

print("\n")

for i in range (0, 101):

    print(f"{i:<5}", end=" ")

    for j in range (0, 101):
        print(f"{i*j:5}", end=" ")
    print()
