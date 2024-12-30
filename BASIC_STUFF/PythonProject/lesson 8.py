# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("kg or pounds? (K or L): ")

if unit not in ["K", "L"]:
    print(f"The {unit} is not correct")
    exit()
else:
    pass

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."

print(f"Your weight is {round(weight, 1)} {unit}, czyli schudnij grubasie!")