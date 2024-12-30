# Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amonut: "))
    if principle < 0:
        print("principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the intrest rate: "))
    if rate < 0:
        print("intrest rate can't be less than or equal to zero")
    else:
        break

while True:
    time = float(input("Enter the principle time in years: "))
    if time < 0:
        print("time can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balans po {time} latach wynosi: {total:.2f} zł")