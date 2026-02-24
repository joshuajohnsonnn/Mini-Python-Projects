print("Dice Roll Sim")

import random
import time
def roll_dice():
    for i in range(1, 7):
        print(f"Rolling the dice... {i}")
        time.sleep(1)
        roll = random.randint(1, 6)
        print(f"Roll {i + 1}: You rolled a {roll}")
        time.sleep(1)
    
roll_dice()
    
while True:
    again = input("Do you want to roll the dice again? (yes/no): ").strip().lower()
    if again == 'yes':
        roll_dice()
    elif again == 'no':
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")


