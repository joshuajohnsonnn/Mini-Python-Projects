import random 

print("Number Guessing Game")

def numberguessinggame():
    Numbers =[1,2,3,4,5,6,7,8,9,0]
    for i in range(2):
        randomnumber = random.choice(Numbers)
        guess = int(input("Guess the number between 0 and 100: "))
        if guess == randomnumber:
            print("Congratulations! You guessed the number correctly.")
        else:
            for j in range(3):
                if guess < randomnumber:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
                guess = int(input("Guess the number between 0 and 100: "))
            print(f"Sorry, You lost.....")
            print(f"The correct number was {randomnumber}.")
            break 
            

while True:
    numberguessinggame()
    playagain = input("Do you want to play again? (yes/no): ").strip().lower()
    if playagain != "yes":
        print("Thanks for playing! Goodbye!")
        break
    
        