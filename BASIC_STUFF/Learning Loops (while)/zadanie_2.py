#Zgadnij liczbę

import random
licznik_prob = 1
liczba_prawidłowa = random.randint(1, 100)

liczba_uzytkownika = int(input("Zgadnij liczbę (od 1 do 100): "))

while liczba_uzytkownika != liczba_prawidłowa:
    licznik_prob += 1
    if liczba_uzytkownika < liczba_prawidłowa:
        print("Za mało! Spróbuj ponownie")
        liczba_uzytkownika = int(input("Zgadnij liczbę (od 1 do 100): "))
    elif liczba_uzytkownika > liczba_prawidłowa:
        print("Za dużo! Spróbuj ponownie")
        liczba_uzytkownika = int(input("Zgadnij liczbę (od 1 do 100): "))

print(f"Brawo, oczekiwana liczba to {liczba_prawidłowa}")
print(f"Udało ci się zgadnąć liczbę za {licznik_prob} razem!")