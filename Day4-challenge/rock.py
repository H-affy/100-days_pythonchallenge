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
game = [rock, paper, scissors]


player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
print(game[player_choice])

computer_choice = random.randint(0, 2)
print(f"The computer choose: ")
print(game[computer_choice])

if player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice == 2 and computer_choice == 1:
    print("You win")
elif player_choice == 2 and computer_choice == 0:
    print("You lose")
elif player_choice == 1 and computer_choice == 0:
    print("You win")
elif computer_choice == player_choice:
    print("it a draw")
elif computer_choice > player_choice:
    print("You lose")
else:
    print("You entered an invalid number")