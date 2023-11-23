#This is from the end of DAY 4 of the coding challenge
#The images were provided by the lesson.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

question = int(input("What do you want to choose? Type 0 for Rock, 1 for Scissors and 2 for Paper. \n\n"))

if question == 0:
  print(rock)
elif question == 1:
  print(scissors)
elif question == 2:
  print(paper)
else:
  print("Please select a choice mentioned.")

print("Computer has chosen:")

random_choice = random.randint(0 , 2)
if random_choice == 0:
  print(rock)
elif random_choice == 1:
  print(scissors)
else:
  print(paper)

#This can be condensed on another day. Its 0055 hours on 11/23/23 and this code worked first try !! Calling it a win tonight
if question == random_choice:
  print("Draw")
elif question == 0 and random_choice == 1:
  print("Winner")
elif question == 0 and random_choice == 2:
  print("Loser")
elif question == 1 and random_choice == 0:
  print("Loser")
elif question == 1 and random_choice == 2:
  print("Winner")
elif question == 2 and random_choice == 0:
  print("Winner")
elif question == 2 and random_choice == 1:
  print("Loser")
