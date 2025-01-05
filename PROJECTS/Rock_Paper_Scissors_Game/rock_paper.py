import random

lista = ("kamien","papier","nozyczki")
wynik_gracz = 0
wynik_bot = 0



while wynik_bot < 3 and wynik_gracz < 3:
    kpn = random.choice(lista)
    wybor = input("Wybierz: kamien, papier albo nozyczki: ").lower()
    if wybor not in lista:
        print("Nie możesz tak zrobić")
        continue
    if wybor == "papier" and kpn == "kamien":
        wynik_gracz += 1
        print(f"TY: {wybor}. ON: {kpn}")
        print("wygrales")
        print(f"Punkty: TY:{wynik_gracz} ON:{wynik_bot}")
    elif wybor == "kamien" and kpn == "nozyczki":
        wynik_gracz += 1
        print(f"TY: {wybor}. ON: {kpn}")
        print("wygrales")
        print(f"Punkty: TY:{wynik_gracz} ON:{wynik_bot}")
    elif wybor == "nozyczki" and kpn == "papier":
        wynik_gracz += 1
        print(f"TY: {wybor}. ON: {kpn}")
        print("wygrales")
        print(f"Punkty: TY:{wynik_gracz} ON:{wynik_bot}")
    elif wybor == kpn:
        print(f"TY: {wybor}. ON: {kpn}")
        print("Remis")
        print(f"Punkty: TY:{wynik_gracz} ON:{wynik_bot}")
    else:
        wynik_bot += 1
        print(f"TY: {wybor}. ON: {kpn}")
        print("Przegrales")
        print(f"Punkty: TY:{wynik_gracz} ON:{wynik_bot}")
else:
    if wynik_gracz == 3:
        print("Wygrales całą gre!")
    else:
        print("Przegrales cala gre, sprobuj ponownie")

