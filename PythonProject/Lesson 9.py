unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")

if unit not in ["C", "F"]:
    print(f"The {unit} is not valid unit.")
    exit()
else:
    pass

temp = float(input("Podaj temperature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    unit = "F"
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    unit = "C"

print(f"Temperatura wynosi {temp}{unit}")