import random
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

player=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

comp = random.randint(0,2)

if(player==0):
  print(rock)
  print("You chose rock")
  if(comp==0):
    print(rock)
    print("Computer chose Rock")
    print("Draw")
  elif(comp==1):
    print(paper)
    print("Computer chose Paper")
    print("You Lose")
  elif(comp==2):
    print(scissors)
    print("Computer chose Scissors")
    print("You Win")
elif(player==1):
  print(paper)
  print("You chose paper")
  if(comp==0):
    print(rock)
    print("Computer chose Rock")
    print("You Win")
  elif(comp==1):
    print(paper)
    print("Computer chose paper")
    print("draw")
  elif(comp==2):
    print(scissors)
    print("Computer chose Scissors")
    print("You Lose")
elif(player==2):
  print(scissors)
  print("You chose scissors")
  if(comp==0):
    print(rock)
    print("Computer chose Rock")
    print("You Lose")
  elif(comp==1):
    print(paper)
    print("Computer chose paper")
    print("You Win")
  elif(comp==2):
    print(scissors)
    print("draw")
else:
  print("Incorrect Input")