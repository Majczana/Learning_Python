# while loop = executes a block of code as long as a condition is true

#name = input("Podaj swoje imię: ")

#while name == "":
#    print("Nie podałeś imienia")
#    name = input("Podaj swoje imię: ")

#print(f"Witaj {name}!")

#age = int(input("Podaj swój wiek: "))

#while age < 0:
#    print("Wiek nie może być liczbą ujemną")
#    age = int(input("Podaj swój wiek: "))

#print(f"Masz {age} lat")

number = 0

while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)
else:
    print("no longer < 5 ")
