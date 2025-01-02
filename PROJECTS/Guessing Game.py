import random

food = ["pizza","pasta","hamburger"]
word = food[random.randint(0, 2)] # Od 0 - 2 bo lista zaczyna się od 0
attempts = 0
guesses = []
word_encript = word
index = 0
#user_name = input("Podaj swoje imię: ").capitalize
#print(f"Powodzenia {user_name}!")


for i in range (len(word_encript)):
    word_encript = word_encript[0:i] + "_" + word_encript[i:1]
print(word_encript)


while "_" in word_encript:
    user_input = input("podaj litere")

    if user_input in guesses:
        (print("juz podales ta litere"))
        continue
    
    guesses.append(user_input)

    if user_input in word:
        for index, char in enumerate(word):
            if char == user_input:
                guesses[index] = user_input
        print("".join(hidden_word))
