import random 

print("Number Guessing Game")
print("Try to guess the number between 0 and 100. You have 5 attempts!")

def numberguessinggame():
    Numbers =[1,2,3,4,5,6,7,8,9,0]
    for i in range(3):
        randomnumber = random.randint(0, 100)
        guess = int(input("Guess the number between 0 and 100: "))
        if guess == randomnumber:
            print("Congratulations! You guessed the number correctly.")
        else:
            for j in range(4):
                if guess < randomnumber:
                    print("Too low! Try again.")
                elif guess > randomnumber:
                    print("Too high! Try again.")
                else:
                    print("Congratulations! You guessed the number correctly.")
                    break
                guess = int(input("Guess the number between 0 and 100: "))
            
            print(f"The correct number was {randomnumber}.")
            break 
            

while True:
    numberguessinggame()
    playagain = input("Do you want to play again? (yes/no): ").strip().lower()
    if playagain != "yes":
        print("Thanks for playing! Goodbye!")
        break
    
        