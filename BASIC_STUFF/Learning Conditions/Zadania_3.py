while True:
    liczba = input("Podaj liczbę całkowitą: ")
    if liczba.lower() == "koniec":
        print("Koniec")
        break
    try:
        liczba = int(liczba)
        l_2 = liczba % 2 == 0
        l_3 = liczba % 3 == 0
        l_5 = liczba % 5 == 0
        l_5_3 = liczba % 5 == 0 and liczba % 3 == 0

        if l_2:
            print(f"Liczba {liczba} jest podzielna przez 2.")
        if l_5_3:
            print(f"Liczba {liczba} jest podzielna jednocześnie przez 3 i 5.")
        elif l_3:
            print(f"Liczba {liczba} jest podzielna przez 3.")
        elif l_5:
            print(f"Liczba {liczba} jest podzielna przez 5.")
        if liczba <= 1:
            print("liczba nie jest podzielna przez 2, 3 ani 5")

    except ValueError:
        print("Podano niepoprawną liczbę. Spróbuj ponownie.")
