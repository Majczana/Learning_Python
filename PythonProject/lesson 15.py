#name = input("podaj swoje imie: ")

#while name == "":
#    print("Nie podales imienia")
#    name = input("podaj swoje imie: ")
#print(f"Hello {name}")

#age = int(input("Podaj datę urodzenia: "))

#while age < 0:
#    print(f"Nie możesz miec {age} lat.")
#    age = int(input("Podaj datę urodzenia: "))

#print(f"You are {age} years old")

#food = input("Enter a food you like (q to quit):")

#while not food == "q":
#    print(f"You like {food}")
#    food = input("Enter another food you like (q to quit):")

#print("bye")

num = int(input(" wpisz liczbę pomiędzy 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input(" wpisz liczbę pomiędzy 1 - 10: "))

print(f"Twoja liczba to {num}")