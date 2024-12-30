counter = 0
liczby = []

print("Podaj dowolne liczby i zakończ program wpisując: stop")
while True: 
    liczba = input("podaj liczbe: ").strip().lower()
    if liczba == "stop":
        print(f"Podałeś {counter} liczb.")
        print(f"Suma podanych liczb wynosi: {sum(liczby):.2f}")
        break
    liczby.append(float(liczba))
    counter += 1