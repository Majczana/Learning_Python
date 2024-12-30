# Kalkulator BMI

koniec = "Dziękujemy za udział"

while True:
    waga = (input("Podaj wagę (kg): "))
    if waga == "koniec":
        print("Dziękujemy za udział")
        break
    wzrost = (input("Podaj wzrost (cm): "))
    if wzrost == "koniec":
        print("Dziękujemy za udział")
        break
    try:
        waga = float(waga)
        wzrost = float(wzrost)
        if waga <= 0 or wzrost <= 0:
            print("Waga i wzrost muszą być liczbami dodatnimi")
            continue
        BMI = waga / ((wzrost / 100) ** 2)
        print(f"Twoje bmi wynosi: {BMI:.2f}")
        if BMI < 18.5:
            print("Niedowaga")
        elif 18.5 <= BMI < 24.9:
            print("Waga prawidłowa 👍")
        elif 25 <= BMI < 29.9:
            print("Nadwaga")
        elif BMI >= 30.0:
            print("Otyłość")
    except ValueError:
        print("Podano nieprawidłowe dane. Spróbuj pomownie")