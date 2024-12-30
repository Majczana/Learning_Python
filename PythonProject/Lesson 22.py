# Shoping cart program

foods = []
prices = []
total = 0

while True:
    food = input("What do you want to eat? (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}:"))
        foods.append(food)
        prices.append(price)

print("------ YOUR CART ------")

for food in foods:
    print(food, end=" ")
for price in prices:
    total += price

print(f"Total: {total}zł")