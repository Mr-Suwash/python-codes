import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
le = int(input("How many letters would you like in your password?\n")) 
sy = int(input(f"How many symbols would you like?\n"))
nu = int(input(f"How many numbers would you like?\n"))

passlist=[]
for i in range(0,le+1):
    passlist+=random.choice(letters)
for i in range(0,nu+1):
    passlist+=random.choice(numbers)
for i in range(0,sy+1):
    passlist+=random.choice(symbols)
random.shuffle(passlist)
password=""
for i in passlist:
    password += i
print(f"Your password is {password}")
