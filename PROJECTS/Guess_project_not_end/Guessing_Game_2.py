import random

guess = []
lista = ["jabłko", "truskawka", "melon"]
slowo = random.choice(lista)
count = len(slowo)
slowo_enc = ("_" * count)

def input_test(slowo):
    if len(slowo) == 1:
        if not slowo.isdigit():
            return True
        return False
    return False
    

while not slowo == slowo_enc:
    user_input = input("Podaj litere:").lower()
    print(slowo_enc)
    if input_test(user_input):
        if user_input in slowo:
            print("zgadles juz to slowo") if user_input in guess else guess.append(user_input)
            print(guess)
            print("trafiles")
        else:
            print(guess)
            print("nie trafiles")
