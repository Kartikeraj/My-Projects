import streamlit as st
import random

words_list = [
    "Apple", "Banana", "Cherry", "Dog", "Elephant", "Frog", "Giraffe", "Hat", "Ice", "Jungle",
    "Kite", "Lemon", "Monkey", "Notebook", "Orange", "Pencil", "Queen", "Rocket", "Sun", "Tiger",
    "Umbrella", "Violin", "Whale", "Xylophone", "Yogurt", "Zebra", "Anchor", "Beach", "Cloud", "Desert",
    "Eagle", "Forest", "Guitar", "Honey", "Island", "Jacket", "Kangaroo", "Lantern", "Mountain", "Nest",
    "Ocean", "Penguin", "Quilt", "Rainbow", "Squirrel", "Tornado", "Underwater", "Volcano", "Window", "X-ray",
    "Yacht", "Zeppelin", "Antelope", "Basket", "Cactus", "Diamond", "Engine", "Firefly", "Glacier", "Horizon",
    "Igloo", "Jigsaw", "Koala", "Lighthouse", "Mermaid", "Nebula", "Octopus", "Panther", "Quasar", "River",
    "Starfish", "Telescope", "Universe", "Vortex", "Waterfall", "Xenon", "Yeti", "Zeppelin", "Alchemy", "Bubble",
    "Crystal", "Dragon", "Emerald", "Fossil", "Galaxy", "Hydra", "Illusion", "Jungle", "Kaleidoscope", "Labyrinth",
    "Mystic", "Nebula", "Oracle", "Phoenix", "Quicksilver", "Riddle", "Spellbound", "Treasure", "Utopia", "Voyager"
]

hangman_steps = [
    r"""
        ------
        |    |
        |    
        |    
        |    
        |    
     --------
    """,
    r"""
        ------
        |    |
        |    O
        |    
        |    
        |    
     --------
    """,
    r"""
        ------
        |    |
        |    O
        |    |
        |    
        |    
     --------
    """,
    r"""
        ------
        |    |
        |    O
        |   /|
        |    
        |    
     --------
    """,
    r"""
        ------
        |    |
        |    O
        |   /|\
        |    
        |    
     --------
    """,
    r"""
        ------
        |    |
        |    O
        |   /|\
        |   / 
        |    
     --------
    """,
    r"""
        ------
        |    |
        |    O
        |   /|\
        |   / \
        |    
     --------
     GAME OVER!
    """
]

def hangman_game():
    if 'random_word' not in st.session_state:
        st.session_state.random_word = random.choice(words_list).lower()
        st.session_state.random_word_len = len(st.session_state.random_word)
        st.session_state.random_word_list = list(st.session_state.random_word)
        st.session_state.chances = 6
        st.session_state.wrong_guesses = 0
        st.session_state.guessed_letters = []
        st.session_state.word_display = ["_"] * st.session_state.random_word_len
        st.session_state.game_over = False

    st.write(hangman_steps[st.session_state.wrong_guesses])
    st.write(" ".join(st.session_state.word_display))

    if not st.session_state.game_over:
        user_letter = st.text_input("Guess a letter:", max_chars=1).lower()

        if user_letter:
            if len(user_letter) != 1 or not user_letter.isalpha():
                st.write("Please enter a single letter.")
            elif user_letter in st.session_state.guessed_letters:
                st.write("You already guessed that letter.")
            else:
                st.session_state.guessed_letters.append(user_letter)

                if user_letter in st.session_state.random_word_list:
                    for i in range(st.session_state.random_word_len):
                        if st.session_state.random_word_list[i] == user_letter:
                            st.session_state.word_display[i] = user_letter
                    if "_" not in st.session_state.word_display:
                        st.write("Congratulations! You guessed the word!")
                        st.session_state.game_over = True
                else:
                    st.session_state.wrong_guesses += 1
                    st.write("Wrong guess!")

                if st.session_state.wrong_guesses == st.session_state.chances:
                    st.write(hangman_steps[st.session_state.wrong_guesses])
                    st.write(f"The word was: {st.session_state.random_word}")
                    st.write("Game over!")
                    st.session_state.game_over = True
    if st.session_state.game_over:
        if st.button("Play Again"):
            for key in st.session_state.keys():
                del st.session_state[key]
            hangman_game()
    return

st.title("Hangman Game")
hangman_game()

st.markdown("---")

st.markdown(
    """
    **Source Code:** [Click here](https://github.com/Kartikeraj/Python_Projects/blob/main/hangman_game1.py)
    """
)

st.markdown(
    """
    **LinkedIn:** [Kartike Raj Choudhary](https://www.linkedin.com/in/kartike-raj-choudhary/)
    """
)

st.markdown(
    """
    **Email:** kartikerajchoudhary@gmail.com
    """
)
