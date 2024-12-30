# function = a block of code which only runs when it is called
# return = statement used to end a function 

def happy_birthday(name, age):
    print(f"Happy birtday to {name}")
    print(f"You are {age} years old")
    print("Happy birtday to you")

#happy_birthday(age=22, name="Filip")

def display_invoice(username, amount, due_date):
    print(f"Czesc {username}")
    print(f"Twój rachunek wynosi: {amount}zł")
    print(f"Wystawiony: {due_date}")

#display_invoice("bro", 1250, "12.02.2024")

def dodawanie(x, y):
    z = x + y
    return z

def odejmowanie(x, y):
    z = x - y
    return z

def mnozenie(x, y):
    z = x * y
    return z

def dzielenie(x, y):
    z = x / y
    return z

#print(dodawanie(15, 10))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


#print(create_name("filip", "majewski"))

def number_args(*args):
    print(args[0]*args[1])

#number_args(1, 3)

def number_kwarg(**number):
    print('My number is: ' + number['integer'])
number_kwarg(integer = '2309')

def function(x):
    print(f"ta liczba {x} jest dalej w funkcji")
    return 2*x

wynik = function(4)
print(wynik)