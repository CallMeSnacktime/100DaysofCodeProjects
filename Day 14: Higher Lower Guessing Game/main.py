from game_data import data
from art import logo,vs
import random
from replit import clear

# Picks a random object
def shuffle():
  return random.choice(data)

# Confirms answer
def who(answer):
  if person_a['follower_count']>person_b['follower_count'] and answer=='a':
    return True
  elif person_a['follower_count']<person_b['follower_count']and answer=='b':
    return True
  elif answer != 'a' and answer !='b':
    print("Invalid Choice")
    return False
  else:
    return False

# Questions for the game
def setup(a,b):
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  return guess

cont=True
while cont==True:
  print(logo)

  person_a=shuffle()
  person_b=shuffle()
 
  score=0
  choice = setup(person_a,person_b)
  game = True
  while game ==True:
    clear()
    print(logo)
    if who(choice) == True:
      score+=1   
      print(f"You're right! Current score: {score}")
      person_a=person_b
      person_b=shuffle()
      choice = setup(person_a,person_b)
    elif who(choice) == False:
      print(f"Sorry, that's wrong. Final score: {score}")   
      game = False
    else:
      print(who(choice))
  play=input("Would like to play again? (Y/N): ").lower()
  if play=='y':
    clear()
    cont=True
  elif play=='n':
    print("Good Bye!")
    cont=False
  else:
    print("Invalid Entry")