import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]


while True:
    user_input = input("\nEnter Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)      # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]

    print("\nComputer picked :", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("\nYou won!\n")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("\nYou won!\n")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("\nYou won!\n")
        user_wins += 1

    elif user_input == computer_pick :
        print("\nDraw! \n")
        user_wins += 1
        computer_wins += 1

    else:
        print("\nYou lost!\n")
        computer_wins += 1

print("\nYou won", user_wins, "times.")
print("The computer won", computer_wins, "times.\n")


print("Goodbye!.....Well Play\n")
