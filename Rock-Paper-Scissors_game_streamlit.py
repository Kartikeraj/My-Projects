import streamlit as st
import random

# Define ASCII Art for Choices
stone = """
 -----
|     |
| ✊  |
|     |
 -----
"""

paper = """
 -----
|     |
|  ✋ |
|     |
 -----
"""

scissors = """
 -----
|     |
|  ✌ |
|     |
 -----
"""

# Streamlit UI
st.title("Rock-Paper-Scissors Game 🎮")

st.subheader("Choose your move:")
col1, col2, col3 = st.columns(3)

# Buttons for selection
user_choice = None
if col1.button("✊ Stone"):
    user_choice = "Stone"
    user2 = stone
elif col2.button("✋ Paper"):
    user_choice = "Paper"
    user2 = paper
elif col3.button("✌ Scissors"):
    user_choice = "Scissors"
    user2 = scissors

# Game Logic
if user_choice:
    list1 = [stone, paper, scissors]
    rand1 = random.choice(list1)

    # Display Choices
    st.subheader("Your Choice:")
    st.code(user2, language="python")

    st.subheader("Computer's Choice:")
    st.code(rand1, language="python")

    # Determine Winner
    if rand1 == user2:
        st.success("It's a Draw! 🤝")
    elif (rand1 == stone and user2 == paper) or \
         (rand1 == paper and user2 == scissors) or \
         (rand1 == scissors and user2 == stone):
        st.success("You Win! 🎉")
    else:
        st.error("You Lose! 😢")

