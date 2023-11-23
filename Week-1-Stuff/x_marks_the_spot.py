#Guess would be letters A-C and numbers 1-3 (A-C = columns / 1-3 = rows) EXAMPLE INPUT = C2
      #   A   B   C
line1 = [" ","️ ","️ "] #   1
line2 = [" "," ","️ "] #   2
line3 = [" ","️ "," "] #   3
map = [line1, line2, line3] # Nested list. REMEMBER Nested Lists start with the outermost list and then goes inside of said list. (map list goes first to reference and then either line1/2/3 list)
print("Hiding your treasure! X marks the spot.")
position = input() # Where the treasure is going

#Broke my brain doing this code
letter_guess = position[0].lower() # Taking the input and assigning it to a spot in a list
letter = ["a", "b", "c"] # Lowercase works better for setting the index letter into the lists
letter_index = letter.index(letter_guess) # Had to lookup what indexing a list does. Taking the letter and assigning it a number value in reference to the map variable/nested list
number_index = int(position[1]) - 1 # Easiest part of the whole thing. Taking the number from the input and subrtacting 1 so it can be placed somewhere in the map variable/nested list
map[number_index][letter_index] = "X"  # Mapping "X" to the position from both index's on lines 13 and 14

#this print line was given as part of the assignment
print(f"{line1}\n{line2}\n{line3}")

#print function will show "X" in the spot from the input
#Wish I did better on my own but had to review from the lesson and be guided a bit through this. Did my best after every two lines to try and solve it on my own. Was able to get up to the map function putting "X" into the index's
