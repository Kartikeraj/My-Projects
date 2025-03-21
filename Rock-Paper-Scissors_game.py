import random

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

user1 = input("Choose Stone,paper or scissors (ST/P/S)").strip().upper()

if user1 == "ST":
    user2 = stone
elif user1 == "P":
    user2 = paper
elif user1 == "S":
    user2 = scissors

list1 = [stone,paper,scissors]
rand1 = random.choice(list1)

print("\nYou chose:")
print(user2)
print("------------------------------------------------------------")
print("Computer chose:")
print(rand1)

if rand1 == user2:
    print("Its a Draw!!!")
elif rand1 == stone and user2 == paper:
    print("You win🎉🎉")
elif rand1 == paper and user2 == stone:
    print("You lose😢")
elif rand1 == scissors and user2 == stone:
    print("You win🎉🎉")
elif rand1 == stone and user2 == scissors:
    print("You lose😢")
elif rand1 == scissors and user2 == paper:
    print("You lose😢")
elif rand1 == paper and user2 == scissors:
    print("You win🎉🎉")