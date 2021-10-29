#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

def start():
  start = False
  print("Welcome to the Number Game! \nI'm thinking of a number between 1 and 100.")
  while start == False:
    
    mode = input("Would you like to play on 'easy' or 'hard' mode? ").lower()
    if mode=='easy':
      chances=10
      start = True
    elif mode=='hard':
      chances=7
      start = True
    else:
      print("Invalid Input")
  return chances

def game():
  lives=start()

  num = random.randint(1,100)
  end = False
 
  while end==False:
    if lives >0:
      guess=int(input(f"{lives} guesses remaining\n* Make a guess: "))
      if guess == num:
        print(f"Good Job!!! The answer was {num}!!")
        end = True
      elif lives>0:
        lives-=1
        if guess>num:
          print(f"Too High.")
        elif guess<num:
          print(f"Too Low.")    
    else:
      print("Better luck next time!!")
      end = True
    

cont =True
while cont==True:
  game()
  play=input("Would like to play again? (Y/N): ").lower()
  if play=='y':
    print("----------------------------")
    cont=True
  elif play=='n':
    print("Good Bye!")
    cont=False
  else:
    print("Invalid Entry")

