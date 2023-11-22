#multiple if statements are used 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the roller coaster!")
  age = int(input("How old are you? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.00.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.00.")
  else:
    bill = 12
    print("Adult tickets are $12.00.")
  wants_photo = input("Would you like photo? Y or N? ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}.")
  
else:
  print("Sorry, you have to grow taller before you can ride.")

#Another example for Multiple IF's

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill = 0
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
if size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
if size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
