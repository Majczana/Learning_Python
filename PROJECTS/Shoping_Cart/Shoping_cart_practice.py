# Shopping cart program

products = []
prices = []
total = 0

while True:
    product = input("Dodaj produkt: ").capitalize()

    if product == "Exit":
        break
    elif product.isalpha():
        price = float(input("Dodaj cene produktu: "))
        products.append(product)
        prices.append(price)
        print(f"Dodano produkt {product}, który kosztuje {price}")
    else:
        print("cos poszlo nie tak")
print("--- TWÓJ KOSZYK ---")
for product in products:
    print(product, end=" ")
print()
for price in prices:
    print(price, end="zł ")
print()
print(F"--- SUMA: {sum(prices)}zł ---")