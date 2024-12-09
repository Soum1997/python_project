letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import  random
# password=""
# for char in range(1,nr_letters+1):
#     password+=random.choice(letters)
# for numb in range(1,nr_symbols):
#     password+=random.choice(numbers)
# for sym in range(1,nr_symbols):
#     password+=random.choice(symbols)
# print(password)

pass_list=[]
for char in range(1,nr_letters+1):
    pass_list.append(random.choice(letters))
for numb in range(1,nr_symbols):
    pass_list.append(random.choice(numbers))
for sym in range(1,nr_symbols):
    pass_list.append(random.choice(symbols))
print(pass_list)

password=""
random.shuffle(pass_list)
for i in pass_list:
    password+=i

print(password)
