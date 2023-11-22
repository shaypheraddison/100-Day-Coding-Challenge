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
random_coin = random.randint(0,1)
if random_coin == 1:
  print("Heads")
else:
  print("Tails")
