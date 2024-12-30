# Operatory Członkostwa i Przypisania

imiona = ["Ala", "Bartek", "Kasia", "Marek"]

while True:
    imie = input("Podaj imię: ").capitalize()
    if imie:
        break
    print("Nie podałeś imienia, podaj imię:")

if imie in imiona:
    print(f"Imie {imie} jest na liście")
else:
    imiona.append(imie)
    print(f"Imie {imie} nie znajduje się na liscie. Właśnie je dodałem")
    print(f"Nowa lista: {imiona}")