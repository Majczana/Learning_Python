# for loops = execute a block of code a fixed number of times.
# interate over a range, string, sequence, etc
# for loops są dobre kiedy musimy wykonać coś określoną ilość razy

#list = [1,2,3,4,5]

#for number in list:
#    print(number)


#lody_dict = {"Imie": "Filip Majewski", "zamówien": 15, "ulubiony smak": ["czeko", "trusk"]}

#for key, value in lody_dict.items(): #.keys / .values / .items
#    print(key, ">>>", value)

smaki = ["czekolada", "truskawka", "Wanillia", "Orzeczhowy", "Oreo"]
dodatki = ["posypką", "płatkami", "polewą"]

for one in smaki:
    for two in dodatki:
        print(one, "z", two)