# ### Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)
# ​
# Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI, oraz podsumowanie informujące o stanie/zaleceniach.
# (Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).

wzrost = int(input("Podaj wzrost w cm"))
waga = float(input("Podaj wagę w kg"))
BMI = waga / ((wzrost/100) ** 2)
print(f"Twoje BMI wynosi {BMI}")
if BMI < 18.5:
    print("Masz niedowagę!")
elif BMI <= 24.9:
    print("Twoja waga jest prawidłowa!")
elif BMI <= 29.9:
    print("Masz nadwagę!")
else:
    print("Masz otyłość!")

