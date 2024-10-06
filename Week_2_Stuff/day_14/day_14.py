from follower_data import data
import random
import os


score = 0

choice_1 = random.choice(data)
choice_2 = random.choice(data)

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def ask_question():
    print(f"\nCompare A: {choice_1["name"]}, a {choice_1["description"]}, from {choice_1["country"]}.")

    print("\nOR\n")

    print(f"Compare B: {choice_2["name"]}, a {choice_2["description"]}, from {choice_2["country"]}.\n")



while True:
    ask_question()
    answer = input("Please choose an answer between Choice A or Choice B: ").upper()

    if answer == "A" and choice_1["follower_count"] > choice_2["follower_count"]:
        clear_console()
        choice_1 = random.choice(data)
        choice_2 = random.choice(data)
        score += 1
    elif answer == "B" and choice_2["follower_count"] > choice_1["follower_count"]:
        clear_console()
        choice_1 = random.choice(data)
        choice_2 = random.choice(data)
        score += 1
    elif answer == "A" and choice_1["follower_count"] < choice_2["follower_count"]:
        choice_1 = random.choice(data)
        choice_2 = random.choice(data)
        print("Sorry you were incorrect.")
        print(f"Score is: {score}")
        break
    elif answer == "B" and choice_2["follower_count"] < choice_1["follower_count"]:
        choice_1 = random.choice(data)
        choice_2 = random.choice(data)
        print("Sorry you were incorrect.")
        print(f"Score is: {score}")
        break
    else:
        print("Please select a correct choice.")