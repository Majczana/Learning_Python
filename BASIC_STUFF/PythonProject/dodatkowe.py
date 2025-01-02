# liczb_cal = int(input("Sprawdz czy liczba jest parzysta: "))
# print("liczba jest parzysta") if liczb_cal % 2 == 0 else print("liczba nie jest nieparzysta")

# liczba_1 = float(input("Podaj pierwszą liczbę: "))
# liczba_2 = float(input("Podaj druga liczbę: "))
# znak = input("Podaj znak operacyjny (+,-,*,/)")


# if znak == "+":
#     print(f"{liczba_1} + {liczba_2} = {liczba_1 + liczba_2}")
# elif znak == "-":
#     print(f"{liczba_1} - {liczba_2} = {liczba_1 - liczba_2}")
# elif znak == "*":
#     print(f"{liczba_1} * {liczba_2} = {liczba_1 * liczba_2}")
# elif znak == "/":
#     if liczba_2 != 0:  # Obsługa dzielenia przez zero
#         print(f"{liczba_1} / {liczba_2} = {liczba_1 / liczba_2}")
#     else:
#         print("Nie można dzielić przez zero!")
# else:
#     print("Nieprawidłowa operacja!")

# n = int(input("Podaj n: "))
# liczby = [0, 1]  # Inicjalizacja ciągu Fibonacciego z dwoma pierwszymi liczbami

# for i in range(2, n):
#     a = liczby[-1]  # Ostatnia liczba w liście
#     b = liczby[-2]  # Przedostatnia liczba w liście
#     liczby.append(a + b)  # Dodaj nową liczbę do listy

# print("Ciąg Fibonacciego:", liczby)

def liczba_pierwsza(liczba):
    liczba = int(liczba)

    if liczba <= 1:
        return False
    for i in range(2, int(liczba**0.5)+ 1):
        if liczba % i == 0:
            return False
    return True

while True:
    liczba = input("Sprawdź czy liczba jest liczbą pierwszą or (exit): ").lower()
    if liczba == "exit":
        break
    print(f"liczba {liczba} jest liczbą pierwszą") if liczba_pierwsza(liczba) == True else print(f"liczba {liczba} nie jest liczbą pierwszą")