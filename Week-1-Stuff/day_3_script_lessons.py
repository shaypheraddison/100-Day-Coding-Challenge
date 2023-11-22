#Learning if/else statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the roller coaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

# Checking if the number is odd or even
number = int(input())

math_number = number % 2

if math_number == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#Learning NESTED IF statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the roller coaster!")
  age = int(input("How old are you? "))
  if age <=18:
    print("Please pay $7.00.")
  else:
    print("Please pay $12.00.")
else:
  print("Sorry, you have to grow taller before you can ride.")

#ELIF statements as well
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the roller coaster!")
  age = int(input("How old are you? "))
  if age < 12:
    print("Please pay $5.00.")
  elif age <= 18:
    print("Please pay $7.00.")
  else:
    print("Please pay $12.00.")
else:
  print("Sorry, you have to grow taller before you can ride.")
