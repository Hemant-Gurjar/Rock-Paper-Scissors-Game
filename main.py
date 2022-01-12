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

#Write your code below this line 👇
import random
game_picture = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice >= 3 or user_choice < 0:
  print("YOU TYPED A WRONG NUMBER. YOU LOOSE")
else:
  print("You choose")
  print(game_picture[user_choice])
 
  computer_choice = random.randint(0, 2)
  print(f"Computer chooses:")
  print(game_picture[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("YOU WIN")
  elif computer_choice == 0 and user_choice == 2:
    print("YOU LOOSE")
  elif computer_choice > user_choice:
    print("YOU LOOSE")
  elif user_choice > computer_choice:
    print("YOU WIN")
  elif computer_choice == user_choice:
    print("IT'S A DRAW")
