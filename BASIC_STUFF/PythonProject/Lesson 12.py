
#name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")

#result = len(name)
#result = name.find("i")
#result = name.rfind("i")
#name = name.capitalize()
#name = name.upper()
#name = name.isdigit()
#result = name.isalpha()
#result = phone_number.count("-")
#phone_number = phone_number.replace("-", "")

username = input("Podaj nazwę użytkownika: ")


if len(username) > 12:
    print("Nazwa nie może być dłuższa niż 12 znaków")
elif not username.find(" ") == -1:
    print("Nazwa nie może zawierać spacji")
elif not username.isalpha():
    print("Nazwa nie może zawierać cyfr")
else:
    print(f"Welcome, {username}")