#default arguments

#defult

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


# print(net_price(500))

# print(net_price(500, 0.1 ))
#print(net_price(500, 0.1, 0.05 ))

#Keyword

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# hello("hello", title="Mr.", last="Elon", first="Musk")

#arbitrary

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments

def add(*args):
    total = 0 
    for arg in args:
        total += arg
    return total

# print(add(1, 2, 3, 4))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

#display_name("Filip", "Tomasz", "Tadeusz" ,"Majewski")


def print_adress (**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_adress(street="Tarnowskiego 11", city="Warta", state="Łódź", )

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    for key, value in kwargs.items():
        print(key, value, end=" ")

#shipping_label("dr.", "spongebob", street="Fake st.123", apt="100" )