# nested loop

rows = int(input("liczba wierszy: "))
columns = int(input("liczba kolumn: "))
symbol = input("Podaj symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
