#Final task during Day 2

print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 15, or 18? "))
people = int(input("How many people to split the bill? "))
tip_math = tip / 100 * bill + bill
bill_per_person = tip_math / people
print(f"Each person should pay: ${bill_per_person:.2f}.")