#Day 7 project to make a hangman game
import random
import hangman_art as stages #file provided by lesson
import hangman_words as word_list #file provided by lesson

chosen_word = random.choice(word_list.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(stages.logo)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):  #Code from the class, lines 17-19
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print("\033[H\033[J") #This removes the previous display to have only one instance of the letters/gallows showing (MAC OS ONLY)
    if guess in display:
      print(f"You have already guessed {guess}.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"{guess} is not in the chosen word, please guess again.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}") #Code from the class

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages.stages[lives])
