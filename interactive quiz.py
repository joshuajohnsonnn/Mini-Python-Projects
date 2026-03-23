import random
import time
print("Welcome to this Interactive Quiz!")
print("You will be asked a series of questions. Try to answer them correctly!")

def interactive_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
            "answer": "B"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
            "answer": "A"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["A) China", "B) Japan", "C) South Korea", "D) Thailand"],
            "answer": "B"
        },
        {
            "question": "What is the largest organ in the human body?",
            "options": ["A) Heart", "B) Liver", "C) Skin", "D) Lungs"],
            "answer": "C"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
            "answer": "C"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "answer": "C"
        }
    ]

    score = 0
    for i in range(9): 
        options = random.choice(questions)
        print(options["question"])

        for option in options["options"]:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == options["answer"]:
            print("Correct!")
            score = score + 1
            time.sleep(1)
        else:
            print(f"Wrong! The correct answer was {options['answer']}.")
            time.sleep(2)
    
    print(f"Your final score is {score} out of 9.")

while True:
    interactive_quiz()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break   