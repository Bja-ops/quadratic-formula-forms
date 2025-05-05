import math

print("Równanie kwadratowe ma postać ax^2 + bx + c")
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))
print()
print("Do jakiej postaci chcesz sprowadzić równanie (kanoniczna, iloczynowa)?")
way = input("Podaj postać: ").lower()

if way == "kanoniczna":
    print("\nPostać kanoniczna to: a(x - p)^2 + q")
    delta = b ** 2 - 4 * a * c
    if delta >= 0:
        p = -b / (2 * a)
        q = -delta / (4 * a)
        print(f"Współrzędne wierzchołka to: p = {p}, q = {q}")
        print(f"Postać kanoniczna: {a}(x - {p})^2 + {q}")
    else:
        print(f"Delta = {delta}. Nie można sprowadzić do postaci kanonicznej (brak pierwiastków rzeczywistych).")

elif way == "iloczynowa":
    print("\nPostać iloczynowa to: a(x - x1)(x - x2)")
    print("Wybierz metodę obliczenia (delta/bez):")
    method = input("Podaj metodę: ").lower()

    if method == "delta":
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = round((-b - math.sqrt(delta)) / (2 * a), 2)
            x2 = round((-b + math.sqrt(delta)) / (2 * a), 2)
            print(f"Postać iloczynowa: {a}(x - {x1})(x - {x2})")
        elif delta == 0:
            x0 = round(-b / (2 * a), 2)
            print(f"Postać iloczynowa: {a}(x - {x0})^2")
        else:
            print(f"Delta = {delta}. Równanie nie ma pierwiastków rzeczywistych.")

    elif method == "bez":
        ac = int(a * c)
        found = False
        for m in range(-abs(ac), abs(ac) + 1):
            if m == 0:
                continue
            if ac % m == 0:
                n = ac // m
                if m + n == int(b):
                    print(f"Znaleziono liczby: {m} i {n}")
                    if a == 1:
                        x1 = -m
                        x2 = -n
                        print(
                            f"Postać iloczynowa: (x {'-' if x1 > 0 else '+'} {abs(x1)})(x {'-' if x2 > 0 else '+'} {abs(x2)})")
                    else:
                        print(f"Postać iloczynowa: {a}(x + ({m}/{a}))(x + ({n}/{a}))")
                    found = True
                    break
        if not found:
            print("Nie udało się znaleźć postaci iloczynowej bez delty.")
    else:
        print("Nieznana metoda. Wpisz 'delta' lub 'bez'.")
else:
    print("Nieznana postać. Wpisz 'kanoniczna' lub 'iloczynowa'.")
