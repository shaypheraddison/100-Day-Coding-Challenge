print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_question = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'\n").lower()

if first_question == "left":
  second_question = input("You arrive at a lake with an island in the middle of it. Type 'wait' to wait for a boat or type 'swim' to swim across to the island.\n").lower()
  
  if second_question == "wait":
    third_question = input("You arrive to the island unharmed. You walk up the path to a house that has three doors to choose. Which one do you select? Type 'yellow' for the yellow door, type 'red' for the red door and type 'blue' for the blue door.\n").lower()
    
    if third_question == "red":
      print("You have found the lost treasure of Atlantis!! Congrats, you have won the game!")
    elif third_question == "yellow":
      print("You have acid sprayed onto your face. Game Over.")
    else:
      print("You activated the trap door and fall into a deep pit. Game Over.")
  else:
    print("You try to swim across and get attached by pirhana. Game Over.")
else:
  print("You have sprung a trap on the ground and fell into a hole. Game Over.")
