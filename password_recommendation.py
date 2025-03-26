# Password Recommendation
# 
# Please keep in mind that I have just started learning Python. 
# So far, I have learned loops and basic functions. 
# Please don't judge me based on this code. 
# I promise to improve and learn more complex methods and better ways to write Python code. 
# For now, please remember that this is my initial stage in learning Python.

import random

# Asking the user for password specifications
length_of_pass = int(input("How long do you want your password to be? "))  # Total length of the password
symbol_counts = int(input("How many symbols do you want in your password? "))  # Number of symbols
number_count = int(input("How many numbers do you want in your password? "))  # Number of numbers

# Lists of characters used for password generation
alphabets_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-']  # List of symbols
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # List of numbers

# Calculating the number of alphabetic characters needed
length_of_alphabets = length_of_pass - (symbol_counts + number_count)

# Method 1: Generating password without using a loop (commented out)
# This method directly selects random characters using `random.choices()`
# and then combines them to form the final password.

# random_symbol = random.choices(symbols_list, k=symbol_counts)
# random_number = random.choices(number_list, k=number_count)
# random_alphanets = random.choices(alphabets_list, k=length_of_alphabets)

# print(random_alphanets)
# print(random_number)
# print(random_symbol)

# combine_all_passwords = random_alphanets + random_number + random_symbol
# random.shuffle(combine_all_passwords)
# password = ''.join(map(str, combine_all_passwords))
# print(password)

# Method 2: Generating password using loops

password = []  # Initializing an empty list to store password characters

# Adding random alphabets to the password list
for i in range(0, length_of_alphabets):
    password += random.choice(alphabets_list)

# Adding random symbols to the password list
for i in range(0, symbol_counts):
    password += random.choice(symbols_list)

# Adding random numbers to the password list
for i in range(0, number_count):
    password.append(random.choice(number_list))

# Shuffling the password list to mix characters randomly
random.shuffle(password)

# Converting the list into a string to create the final password
password_final = ''.join(map(str, password))

# Printing the generated password
print(password_final)
