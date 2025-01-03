pytania = ("1.Jakie są podstawowe typy danych w Pythonie?", "2.Co robi funkcja len() w Pythonie?",
           "3.Jak zdefiniować zmienną w Pythonie?",
           "4.Jakie jest znaczenie pętli for w Pythonie?", "5.Jak w Pythonie sprawdzić, czy liczba jest większa od 10?")

opcje = (
    (
        "A) int, float, str, bool",
        "B) decimal, double, char, logical",
        "C) integer, fraction, string, boolean"
    ),  # 1. Jakie są podstawowe typy danych w Pythonie?
    (
        "A) Zwraca długość listy, ciągu znaków lub innego obiektu.",
        "B) Konwertuje tekst na małe litery.",
        "C) Usuwa ostatni element z listy."
    ),  # 2. Co robi funkcja len() w Pythonie?
    (
        "A) Używając słowa kluczowego var, np. var x = 10.",
        "B) Po prostu przypisując wartość, np. x = 10.",
        "C) Deklarując typ zmiennej, np. int x = 10."
    ),  # 3. Jak zdefiniować zmienną w Pythonie?
    (
        "A) Iteruje po określonej liczbie elementów w zbiorze danych.",
        "B) Powtarza kod nieskończoną ilość razy.",
        "C) Służy do definiowania funkcji."
    ),  # 4. Jakie jest znaczenie pętli for w Pythonie?
    (
        "A) if x >= 10:",
        "B) if x > 10:",
        "C) if x > 10 then:"
    )   # 5. Jak w Pythonie sprawdzić, czy liczba jest większa od 10?
)

odpowiedzi = ("A","B","C","A","A")
guesses = []
wynik = 0
nr_pyt = 0

for pytanie in pytania:
    print("-------------------------")
    print(f"{pytanie}")
    for opcja in opcje[nr_pyt]:
        print(opcja)

    guess = input("Zgadnij odpowiedź (A,B,C): ").upper()
    guesses.append(guess)
    if guess == odpowiedzi[nr_pyt]:
        wynik += 1
        print(f"odpowiedz prawidłowa!")
    else:
        print("zla odpowiedz")
    nr_pyt += 1

print("Twoje odpowiedzi:")
print()
for guess in guesses:
    print(guess, end=" ")
print()
for odpowiedz in odpowiedzi:
    print(odpowiedz, end=" ")
print()
print("-------------------------")
wynik = int(wynik / len(pytania) * 100)
print(f"Twój wynik to: {wynik}%")
print("-------------------------")