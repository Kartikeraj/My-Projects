import streamlit as st
import random

st.header("Welcome to the Coin Toss Game!")
st.divider()
st.markdown("To play the game, click on **Heads** or **Tails** below.")

# Creating two columns for buttons
col1, col2 = st.columns(2)

if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
    st.session_state.result = None

# Button logic
with col1:
    if st.button("Heads", type="primary"):
        st.session_state.user_choice = "H"

with col2:
    if st.button("Tails", type="secondary"):
        st.session_state.user_choice = "T"

# Coin toss logic
if st.session_state.user_choice:
    random_coin = random.choice(["H", "T"])
    result_text = "HEADS" if random_coin == "H" else "TAILS"

    if st.session_state.user_choice == random_coin:
        st.success(f"🎉 You won! It's **{result_text}**!")
    else:
        st.error(f"❌ You lost! It's **{result_text}**.")

    # Reset choice after displaying result
    st.session_state.user_choice = None

