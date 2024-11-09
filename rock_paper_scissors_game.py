import random

# ASCII art for the game
r_p_s = """
  _____    _____     _____ 
 |  __ \  |  __ \   / ____|
 | |__) | | |__) | | (___  
 |  _  /  |  ___/   \___ \ 
 | | \ \  | |       ____) |
 |_|  \_\ |_|      |_____/ 
"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of choices
rock_paper_scissors = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

print(r_p_s)
print("Welcome to Rock, Paper, Scissors game!")

# Initializing scores
user_score = 0
computer_score = 0

# Main game loop
continue_game = True
while continue_game:
    try:
        # Getting a user choice
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
        # Validate user input
        if choice < 0 or choice >= 3:
            print("Invalid choice, you lose this round!")
            computer_score += 1
            continue
    except ValueError:
        print("Invalid input! Please enter 0, 1, or 2.")
        continue
    
    # Display user choice
    print(f"\nYou chose: {choices[choice]}")
    print(rock_paper_scissors[choice])

    # Generate and display computer choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {choices[computer_choice]}")
    print(rock_paper_scissors[computer_choice])

    # Determine the result
    if choice == computer_choice:
        print("It's a draw!\n")
    elif (choice == 0 and computer_choice == 2) or \
         (choice == 1 and computer_choice == 0) or \
         (choice == 2 and computer_choice == 1):
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1

    # Display current score
    print(f"Current Score -> You: {user_score} | Computer: {computer_score}\n")

    # Ask if user wants to play again
    user_choice = input("Do you want to play again? Type 'yes' to continue playing or 'no' to stop playing.\n").lower()
    if user_choice == "no":
        print("Thanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        continue_game = False
