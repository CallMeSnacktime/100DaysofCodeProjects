from replit import clear
from art import logo

table={}

next=True
# Loop to get entries
while next:
  clear()
  print(logo)
  name=input("What is your name?\n")
  bid=int(input("How much would you like to bid? (No dollar signs please)\n"))
  table[name]=bid
  cont=input("Is there another bidder? (Y/N)\n").lower()
  if cont !="y":
    next=False

#Check for winner
top=0
winner=""
for bidder in table:
  if table[bidder] > top:
    winner=bidder
    top = table[winner]
print(f"{winner} is the top bidder with ${top}")


