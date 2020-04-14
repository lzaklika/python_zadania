# ### Zadanie 2.2 | Choinka
# ​
# Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:
# ​
# ```
#     *
#   * * *
# * * * * *
# ```
pietro = int(input("Ile pięter ma mieć ""choinka""?"))
liczba_gwiazdek = 1
liczba_spacji = pietro - 1

znak_gwiazdka = "* "
znak_spacja = "  "

for i in range(1, pietro + 1):
    for j in range(0, liczba_spacji):
        print(znak_spacja, end="")
    for k in range(0, liczba_gwiazdek):
        print(znak_gwiazdka, end="")
    print()
    liczba_gwiazdek += 2
    liczba_spacji -= 1



# while i <= pietro:
#     if liczba_gwiazdek < (2 * pietro - 1):
#         for i in (1, pietro - 1):
#             print(znak_spacja, end="")
#         for i in (1, liczba_gwiazdek):
#             print(znak_gwiazdka, end="")
#         liczba_gwiazdek += 2
#         pietro -= 1
#         print()
#





