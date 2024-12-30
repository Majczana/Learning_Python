import time

my_time = int(input("Enter time in secounds: "))

for x in range(my_time, 0, -1):
    secounds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{secounds:02}")
    time.sleep(1)

print("już")

