#Typecasting = Formatowanie typów zmiennych
# str(), int(), float(), bool()
from traceback import print_tb

name = "Filip Majewski"
age = 22
gpa = 3.2
is_student = True

is_empty = bool(name)

if is_empty:
    print("Wszystko dobrze")
else:
    print("Pole jest puste")