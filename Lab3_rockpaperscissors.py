# Software development method
# Game will first greet the player
# The Elements is a game based on rock paper scissors 
# where the player is given a choice to choose air, 
# earth, water, fire, and spirit.
# The computer player randomly chooses their move, and then we determine who won and display a "You won!" or a "You lost!" message to the player

print("Hello oh, young padawan to the elite ultra-interactive gaming software called 'The Elements'.")
print("Type 1 for Air, 2 for Earth, 3 for Water, 4 for Fire, or 5 for Spirit to select your Element if you dare.")

player_choice = int(input())

if (player_choice > 5 or player_choice < 1):
    print("Wrong freaking number, get a grip before playing this hard-core game!")
    player_choice2 = int(input())
    if (player_choice2 > 5 or player_choice2 < 1):
        print("Sorry you just cannot deal with numbers. Not my problem. Goodbye!")
        exit()
    else: 
        player_choice = player_choice2

print(f"You chose {player_choice or player2_choice}")

# We could check here if the number is a valid elemental name
# We could also generate the computer player's move choice here too

import random
ai_choice = random.randint(1,5)
print(f"The AI chose {ai_choice}")

if (player_choice == 1 and ai_choice == 2) or (player_choice == 2 and ai_choice == 3) or (player_choice == 3 and ai_choice == 4) or (player_choice == 4 and ai_choice == 5) or (player_choice == 5 and ai_choice == 1):
    print("Haha, you are actually SOOOOOO dumb. I would say better luck next time.......IF I CARED!")
elif (player_choice == 2 and ai_choice == 1) or (player_choice == 3 and ai_choice == 2) or (player_choice == 4 and ai_choice == 3) or (player_choice == 5 and ai_choice == 4) or (player_choice == 1 and ai_choice == 5):
    print("You somehow won this extremely difficult game, you must have hacked my systems! Cheater!")
else:
    print("At least you didn't win. LMAO, you gotta try again and again and again!")