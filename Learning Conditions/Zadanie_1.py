age = (input("Podaj wiek: "))
age = int(age)
if age < 0:
    print("Jesteś jeszcze w planach")
elif age < 18:
    print("Niepełnoletni")
elif age == 18:
    print("Masz 18 lat")
elif age == 100:
    print("Sto lat!")
elif age > 109:
    print("Jesteś za stary")
elif age > 18:
    print("Pełnoletni")
else:
    print("Coś poszło nie tak")