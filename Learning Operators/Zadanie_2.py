a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

wyniki = [a > b and a < c, b == c or b > a, a == c]

print(f"{a} > {b} i {a} < {c}: {wyniki[0]}")
print(f"{b} == {c} lub {b} > {a}: {wyniki[1]}")
print(f"{a} == {c}: {wyniki[2]}")