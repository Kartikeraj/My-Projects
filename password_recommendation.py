# password recommendation

import random

length_of_pass = int(input("How much long password do you want?"))

symbol_counts = int(input("How many symbols do you want in your password?"))

number_count = int(input("How many numbers do you want in your password?"))

alphabets_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

symbols_list = ['!','@','#','$','%','^','&','*','(',')','-']

number_list = [0,1,2,3,4,5,6,7,8,9]

random_symbol = random.choices(symbols_list,k=symbol_counts)

random_number = random.choices(number_list,k=number_count)

length_of_alphabets = length_of_pass - (symbol_counts + number_count)

random_alphanets = random.choices(alphabets_list,k=length_of_alphabets)

print(random_alphanets)
print(random_number)
print(random_symbol)

