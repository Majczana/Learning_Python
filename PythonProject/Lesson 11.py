# Conditional expression = (Ternary operator) x if condition else Y

num = 5
a = 6
b = 7
age = 17
temp = 29
user_role = "admin"

#result = "Even" if num % 2 == 0 else "ODD"
#print("Positive" if num > 0 else "Negative")
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Kido"
#weather = "HOT" if temp >= 30 else "Warm"
access_level = "Full Access" if user_role == "admin" else "not access"

print(f"You have {access_level}")