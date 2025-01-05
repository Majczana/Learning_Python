import time

menu = {"kawa": 3.50, "herbata": 4.50, 
        "kawa z mlekiem": 5.50, 
        "herbata z mlekiem": 6.50, 
        "kawa z cukrem": 7.50, 
        "herbata z cukrem": 8.50}


cart = []
total = 0

print("---------Nasze Menu----------")
for product, price in menu.items():
    print(f"{product:20} {price:.2f}zł")
print("------------------------------")

def koszyk(cart, total):
    print('Twój koszyk:')
    time.sleep(1)
    print("---------------------")
    for produkt in cart:
        print(produkt, end=", ")
    print()
    print("---------------------")
    time.sleep(1)
    print(f"Wartość koszyka: {total:.2f}zł")

while True:
    select = input("Dodaj produkt do koszyka: ")
    if select.lower() == "q":
        koszyk (cart, total)
        break

    if select in menu:
        cart.append(select)
        total += menu[select]
        time.sleep(1)
        print("*Produkt dodany*")
        time.sleep(1)
        koszyk(cart, total)
        print()
    else:
        print("*Produktu nie ma na liście, spróbuj ponownie*")

