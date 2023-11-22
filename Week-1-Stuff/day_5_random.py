import random
#random whole numbers
random_integer = random.randint(1, 50)
print(random_integer)

#random float numbers
random_decimal = random.random()
random_float = random.random() * 5
print(random_decimal)
print(random_float)

#random coin flip to show heads or tails
#import random
random_coin = random.randint(0,1)
if random_coin == 1:
  print("Heads")
else:
  print("Tails")

#select a random name from a list practice
#import random
names = ["Greg", "Shaun", "Liam", "Kara", "Liz", "Dave"]
names.append("Spencer")
random_name = random.choice(names)
print(f"{random_name} is going to pay for the meal today!")
