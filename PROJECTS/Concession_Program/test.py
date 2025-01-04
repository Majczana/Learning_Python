menu = {"kawa": 3.50, "herbata": 4.50, 
        "kawa z mlekiem": 5.50, 
        "herbata z mlekiem": 6.50, 
        "kawa z cukrem": 7.50, 
        "herbata z cukrem": 8.50}

cart = []

select = input("Dodaj produkt do koszyka: ")
print(menu.get(select,))