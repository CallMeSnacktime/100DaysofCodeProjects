#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pword =""
for each in range(1,nr_letters+1):
  pword += random.choice(letters)
for each in range(1,nr_symbols+1):
  pword += random.choice(numbers)
for each in range(1,nr_numbers+1):
  pword += random.choice(symbols)

print("Easy Level Answer: " + pword)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#My Solution
#i= len(pword)
#rword=""
#pword=list(pword)
#for each in range(0,i):
#  x=random.randint(0,len(pword)-1)
#  rword = rword+pword[x]
#  pword.pop(x)
#print("Randomly Generated: " + rword)

pwordList = []
for each in range(1,nr_letters+1):
  pwordList.append(random.choice(letters))
for each in range(1,nr_symbols+1):
  pwordList.append(random.choice(numbers))
for each in range(1,nr_numbers+1):
  pwordList.append(random.choice(symbols)) 

print(pwordList)
random.shuffle(pwordList)
print(pwordList)
print("Hard Level Answer: "+ "".join(pwordList))
