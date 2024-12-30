def temp_change(temp, unit):
    if unit == "C":
        return round(temp * (9/5) + 32, 1)
    elif unit == "F":
        return round((temp - 32) * (5/9), 1)

while True:

    unit = input("Podaj jednostkę (C/F):").upper()
    if unit not in ["C","F"]:
        print(f"{unit} to zła jednostka.")
        continue

    temp = input(f"Podaj temperature w {unit}: ")

    try:
        temp = float(temp)
    except ValueError:
        print(f"{temp} nie jest liczbą. Spróbuj ponownie.")
        continue

    print(temp_change(temp, unit))

    print("Enter to continue")
    print("Exit to leave")

    decyzja = input("").lower()
    if decyzja == "exit":
        print("Dzięki za przetestowanie")
        break