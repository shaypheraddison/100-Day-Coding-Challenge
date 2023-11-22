#Calculating how many time the letters from LOVE and TRUE show up in two names(from input)
#Adding the two names together in a string, converting to an int and deciding if they love each other or not
# THIS WAS HARD to learn and make sure I had it right on 11/20/23 @ 2310 hours

print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?

combined_names = name1 + name2
lower_names = combined_names.lower()

#learned this part from the lesson, my version included lists that would work until the last test input failed
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

#This is what I had during the lesson and was able to create 
score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
