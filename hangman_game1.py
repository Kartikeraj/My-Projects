import random
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

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
    """
        ------
        |    |
        |    
        |    
        |    
        |    
     --------
    """,
    """
        ------
        |    |
        |    O
        |    
        |    
        |    
     --------
    """,
    """
        ------
        |    |
        |    O
        |    |
        |    
        |    
     --------
    """,
    """
        ------
        |    |
        |    O
        |   /|
        |    
        |    
     --------
    """,
    """
        ------
        |    |
        |    O
        |   /|\\
        |    
        |    
     --------
    """,
    """
        ------
        |    |
        |    O
        |   /|\\
        |   / 
        |    
     --------
    """,
    """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |    
     --------
     GAME OVER!
    """
]

random_word = random.choice(words_list).lower()
random_word_len = len(random_word)
random_word_list = list(random_word)

chances = 6
wrong_guesses = 0
guessed_letters = []
word_display = ["_"] * random_word_len

while wrong_guesses < chances:
    clear_terminal()
    print(hangman_steps[wrong_guesses])
    print(" ".join(word_display))
    user_letter = input("Guess a letter: ").lower()

    if len(user_letter) != 1 or not user_letter.isalpha():
        print("Please enter a single letter.")
        continue

    if user_letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(user_letter)

    if user_letter in random_word_list:
        for i in range(random_word_len):
            if random_word_list[i] == user_letter:
                word_display[i] = user_letter
        if "_" not in word_display:
            clear_terminal()
            print(hangman_steps[wrong_guesses])
            print(" ".join(word_display))
            print("Congratulations! You guessed the word!")
            break
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if wrong_guesses == chances:
    clear_terminal()
    print(hangman_steps[wrong_guesses])
    print(f"The word was: {random_word}")
    print("Game over!")