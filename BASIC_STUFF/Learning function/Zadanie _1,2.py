def palindrom(nazwa):
    return nazwa == nazwa[::-1]

print("Wpisz 'stop', aby zakończyć program.")
while True:
    nazwa = input("Podaj nazwę: ").strip().lower()  # Usuwamy zbędne spacje i zamieniamy na małe litery
    
    if not nazwa:  # Sprawdzamy, czy wprowadzono pusty string
        print("Nieprawidłowa nazwa, wpisz ponownie.")
        continue
    
    if nazwa == "stop":
        print("Zatrzymałeś program.")
        break

    if palindrom(nazwa):
        print(f"Słowo '{nazwa}' jest palindromem i od tyłu wygląda tak samo: '{nazwa}'.")
    else:
        print(f"Słowo '{nazwa}' NIE jest palindromem, a od tyłu wygląda tak: '{nazwa[::-1]}'.")