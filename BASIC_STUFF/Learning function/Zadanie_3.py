def create_list(od, do):
    return list(range(od, do + 1))

def liczby_pierwsze(liczby):
    liczby_pierwsze = []
    for liczba in liczby:
        if liczba > 1:  # Liczby pierwsze są większe od 1
            for i in range(2, int(liczba**0.5) + 1):  # Sprawdzanie dzielników do pierwiastka kwadratowego
                if liczba % i == 0:
                    break
            else:
                liczby_pierwsze.append(liczba)  # Dodajemy liczbę, jeśli nie ma dzielników
    return liczby_pierwsze

# Główna część programu
od = int(input("Wpisz od: "))
do = int(input("Wpisz do: "))

liczby = create_list(od, do)
print(f"Zakres liczb: {liczby}")

pierwsze = liczby_pierwsze(liczby)
print(f"Liczby pierwsze w zakresie od {od} do {do}: {pierwsze}")
