import random

low = 1
high = 100
number = random.random()
options = ("rock", "paper", "scissors")
cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
option = random.choice(options)
print(number)
print(option)
random.shuffle(cards)
print(cards)
