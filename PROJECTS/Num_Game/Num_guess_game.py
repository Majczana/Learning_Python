
def play_game():
    import random
    liczba = random.randint(1,100)
    lives = 10

    print("Witaj w grze ZGADNIJ LICZBĘ!")
    print("W tej grze musisz zgadnąć liczbę od 1 do 100")
    print("Masz 10 prób jeżeli ci się uda wygrywasz!")
    is_running = True

    while lives != 0:
        guess = int(input("Zgadnij liczbę: "))
        lives -= 1
        if guess == liczba:
            print("wygrales")
            print(f"Pozostało ci {lives} życie. Brawo!")
            break
        elif guess > liczba:
            print("Spróbuj mniejszą liczbę")
            print(f"Pozostało ci {lives}")
        elif guess < liczba:
            print("Spróbuj większą liczbę")
            print(f"Pozostało ci {lives}")
    else:
        print("Przegrałeś... skonczyły ci się życia")
        print(f"Wylosowaną liczbą była liczba: {liczba}")
        print("Spróbuj ponownie")
play_game()