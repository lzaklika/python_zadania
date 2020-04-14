# ### Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)
# ​
# Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.
# ​
# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.
# ​
# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem. I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.

print(">>> WERSJA 1 <<<")
ziemniaki_cena = float(input("Ile kosztuje kilogram ziemniaków?"))
print(f"Za 5 kilo ziemniaków należy zapłacić {ziemniaki_cena * 5} PLN")

print(">>> WERSJA 2 <<<")
ziemniaki_cena = float(input("Ile kosztuje kilogram ziemniaków?"))
ziemniaki_ilosc = float(input("Ile kilogramów ziemniaków chcesz kupić?"))
print(f"Za {ziemniaki_ilosc} kg ziemniaków należy zapłacić {ziemniaki_cena * ziemniaki_ilosc} PLN")

print(">>> WERSJA 3 <<<")
ziemniaki_cena = float(input("Ile kosztuje kilogram ziemniaków?"))
ziemniaki_ilosc = float(input("Ile kilogramów ziemniaków chcesz kupić?"))
banany_cena = float(input("Ile kosztuje kilogram bananów?"))
banany_ilosc = float(input("Ile kilogramów bananów chcesz kupić?"))
print(f"Za {ziemniaki_ilosc} kg ziemniaków po {ziemniaki_cena} PLN/kg oraz za {banany_ilosc} kg bananów po {banany_cena} PLN/kg musisz zapłacić łącznie {ziemniaki_cena * ziemniaki_ilosc + banany_cena * banany_ilosc} PLN.")