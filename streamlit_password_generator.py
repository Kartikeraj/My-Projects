import streamlit as st
import random

st.title("Password Recommendation")

# Asking the user for password specifications
length_of_pass = st.number_input("How long do you want your password to be?", min_value=4, max_value=50, value=12)
symbol_counts = st.number_input("How many symbols do you want in your password?", min_value=0, max_value=length_of_pass, value=2)
number_count = st.number_input("How many numbers do you want in your password?", min_value=0, max_value=length_of_pass - symbol_counts, value=2)

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

# Generating password using loops
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

if st.button("Generate Password"):
    if symbol_counts + number_count > length_of_pass:
        st.error("Sum of symbols and numbers cannot exceed password length!")
    else:
        st.success(f"Generated Password: {password_final}")

st.markdown("[Source Code](https://github.com/Kartikeraj/My-Projects/blob/main/password_recommendation.py)")
st.markdown("[Connect on LinkedIn](https://www.linkedin.com/in/kartike-raj-choudhary/)")

st.write("Made by **Kartike Raj Choudhary**")
