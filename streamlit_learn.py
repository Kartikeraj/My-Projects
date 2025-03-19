# import streamlit as st
# import random

# st.header("Welcome to Coin toss game")
# st.divider()
# # st.subheader("To play the game Type what do you want Heads or Tails by typing H/T in the below chatbox")
# st.markdown("To play the game Type what do you want Heads or Tails by typing H/T in the below chatbox")

# col1, col2 = st.columns(2)

# with col1:
#     st.button("Heads", type='primary')

# with col2:
#     st.button("Tails", type='secondary')

# code = """

# choose = input(" Head or Tails? (H/T): ").strip().upper()
# random_coin = random.randint(1,2)


# if random_coin == 2:
#     result = "TAILS"
#     win = "T"
# elif random_coin == 1:
#     result = "HEADS"
#     win = "H"

    
# if choose != "H" and choose != "T":
#      print("Choose a correct input you loser")
# elif choose == win :
#     print(f"You are the winner , Its {result}")
# else:
#      print(f"You are a fucking loser, Its {result}")

# """

# st.code(code,language="python")
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

