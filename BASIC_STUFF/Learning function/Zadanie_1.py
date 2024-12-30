
#def palindrom(nazwa):
#    nazwa_2 = nazwa[::-1]
#    if nazwa == nazwa_2:
#        return True
#    else:
#        return False
    
def palindrom(nazwa):
    return nazwa == nazwa[::-1]


print("Wpisz 'stop', aby zakończyć program.")
while True:
    nazwa = input("Podaj nazwę: ").strip().lower()
    while nazwa == "":
        nazwa = input("Nieprawidłowa nazwa, wpisz ponownie: ").lower()
    if nazwa == "stop":
        print("zatrzymałeś program")
        break
    nazwa_2 = nazwa[::-1]
    if palindrom(nazwa):
        print(f"Słowo {nazwa} jest palindromem i od tyłu wygląda tak: {nazwa_2}")
    else:
        print(f"Słowo {nazwa} NIE jest palindromem, a od tyłu wygląda tak: {nazwa_2}")