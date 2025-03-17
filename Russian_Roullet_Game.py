# print("Welcome to Russian Roulette")
# character = input("Choose your charater name ")
# print(f"{character} was once a highly trained soldier, but his own commander betrayed him.\n "
#       "His team was killed, his family taken, and his life destroyed.\n "
#       "After years of chasing revenge, he realized he had nothing left to live for.\n "
#       "Now, he sits in a dark Russian bar, staring at a loaded revolver.\n "
#       f"Around him, dangerous men place their bets. But {character} isn’t here for money.\n "
#       "He’s here to see if fate wants him to live or die.")

# play1 = input("Do you want to play? Y or N")
# if play1 == "Y":
#     gun = input("Select your gun!\n"
#           " 1) Colt Python .357 Magnum – A classic revolver, known for its powerful shot and smooth trigger pull. Used by law enforcement and gun enthusiasts. Type C if you want this gun\n "
#           " 2) Nagant M1895 – A historic Russian revolver, fitting the setting. It has a unique sealed-cylinder mechanism, making it different from other revolvers. Type N if you want this gun\n "
#           " 3) Smith & Wesson Model 19 – A reliable and iconic revolver, popular among detectives and military officers, known for its balance and accuracy.Type S if you want this gun\n ")
#     if gun =="C":
#         gun1 = "Colt Python"
#     elif gun == "N":
#         gun1 = "Nagant M11895"
#     else:
#         gun1 = "Smith & Wesson Model 19"
#     print(f"You are ready to play with {gun1}")
#     first1 = input("do you want to pull the trigger first? Y or N")
#     if first1 == "Y":
#         print("clik.... clik....."
#         "you are saved")
#     elif first1 == "N":
#         print("click........Your opponent is saved!!")
#         print("now its your turn")
#     scared = input("do you want to quit?? Y or N")
#     if scared == "Y":
#         print("""
#                 ██████   ███████   █      ██    ███████
#                 ██   █   ██   ██   ████   ██    ██ 
#                 ██████   ███████   ██ ██  ██    ██   ████
#                 ██   █   ██   ██   ██  ██ ██    ██     ███
#                 ██████   ██   ██   ██    ███    █████████   █ █ █ █ █ █ █ █ █ █ █
#                 """)
#         print("BANG... BANG... The person next to you pulls the trigger.\n"
#               "You collapse, everything fades to black.\n"
#               "Your game is over")
#     else:
#         print("Glad to see you're interested!!💀")
#         second = input("Now its your chance to pull the tirgger!!!!  Press Y to Pull the trigger")
#     if second == "Y":
#         print("""
#                 ██████   ███████   █      ██    ███████
#                 ██   █   ██   ██   ████   ██    ██ 
#                 ██████   ███████   ██ ██  ██    ██   ████
#                 ██   █   ██   ██   ██  ██ ██    ██     ███
#                 ██████   ██   ██   ██    ███    █████████   █ █ █ █ █ █ █ █ █ █ █
#                 """)
#         print("BANG... BANG... The person next to you pulls the trigger.\n"
#               "You collapse, everything fades to black.\n"
#               "Your game is over")
# else:
#     print(" Go home! "
#            "you are a looser "
#            "you are a piece of shit ")

print("Welcome to Russian Roulette")
character = input("Choose your character name: ")

print(f"{character} was once a highly trained soldier, but his own commander betrayed him.\n"
      "His team was killed, his family taken, and his life destroyed.\n"
      "After years of chasing revenge, he realized he had nothing left to live for.\n"
      "Now, he sits in a dark Russian bar, staring at a loaded revolver.\n"
      f"Around him, dangerous men place their bets. But {character} isn’t here for money.\n"
      "He’s here to see if fate wants him to live or die.")

play1 = input("Do you want to play? (Y/N): ").strip().upper()

if play1 == "Y":
    gun = input("Select your gun!\n"
                " 1) Colt Python .357 Magnum – A classic revolver, known for its powerful shot and smooth trigger pull. Type C if you want this gun.\n"
                " 2) Nagant M1895 – A historic Russian revolver with a unique sealed-cylinder mechanism. Type N if you want this gun.\n"
                " 3) Smith & Wesson Model 19 – A reliable and iconic revolver, popular among detectives. Type S if you want this gun.\n"
                "Enter your choice (C/N/S): ").strip().upper()

    if gun == "C":
        gun1 = "Colt Python .357 Magnum"
    elif gun == "N":
        gun1 = "Nagant M1895"
    else:
        gun1 = "Smith & Wesson Model 19"

    print(f"You are ready to play with {gun1}.")

    first1 = input("Do you want to pull the trigger first? (Y/N): ").strip().upper()
    
    if first1 == "Y":
        print("Click... Click... You are saved!")
        print("Your opponent is also saved")
    elif first1 == "N":
        print("Click... Your opponent is saved!!\nNow it's your turn.")

    scared = input("Do you want to quit? (Y/N): ").strip().upper()

    if scared == "Y":
        print("""
        ██████   ███████   █      ██    ███████
        ██   █   ██   ██   ████   ██    ██ 
        ██████   ███████   ██ ██  ██    ██   ████
        ██   █   ██   ██   ██  ██ ██    ██     ███
        ██████   ██   ██   ██    ███    █████████  
        """)
        print("BANG... BANG... The person next to you pulls the trigger.\n"
              "You collapse, everything fades to black.\n"
              "Your game is over.")
    else:
        print("Glad to see you're interested! 💀")
        second = input("Now it's your chance to pull the trigger! Press Y to pull the trigger: ").strip().upper()

        if second == "Y":
            print("""
            ██████   ███████   █      ██    ███████
            ██   █   ██   ██   ████   ██    ██ 
            ██████   ███████   ██ ██  ██    ██   ████
            ██   █   ██   ██   ██  ██ ██    ██     ███
            ██████   ██   ██   ██    ███    █████████  
            """)
            print("BANG... BANG....\n"
                  "You collapse, everything fades to black.\n"
                  "Your game is over.")

else:
    print("Go home! You are a loser. You are a piece of shit.")

