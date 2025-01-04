capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Poland": "Warsaw",}

#print(dir(capitals))


# kraj = input("podaj kraj")

# if capitals.get(kraj):
#     print(capitals.get(kraj))
# else:
#     print("Tego kraju nie ma na liscie")


# keys = capitals.keys()
# value = capitals.values()

# for key in keys:
#     print(key)
# for val in value:
#     print(val)

items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")
#    print(items)