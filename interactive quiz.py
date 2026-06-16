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
        },
        
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
            "answer": "B"
        },
        
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"],
            "answer": "C"
        },
        
        {
            "question": "Which ocean is the largest?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["A) Tomato", "B) Avocado", "C) Onion", "D) Pepper"],
            "answer": "B"
        },
        
        {
            "question": "Who is known as the Father of Computers?",
            "options": ["A) Charles Babbage", "B) Alan Turing", "C) Bill Gates", "D) Steve Jobs"],
            "answer": "A"
        },
        
        {
            "question": "What is the currency of Japan?",
            "options": ["A) Yen", "B) Dollar", "C) Euro", "D) Pound"],
            "answer": "A"
        },
        
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A) Gold", "B) Oxygen", "C) Silver", "D) Iron"],
            "answer": "B"
        },
        
        {
            "question": "What is the tallest mountain in the world?",
            "options": ["A) K2", "B) Kangchenjunga", "C) Mount Everest", "D) Lhotse"],
            "answer": "C"
        },
        
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A) Venus", "B) Earth", "C) Mercury", "D) Mars"],
            "answer": "C"
        },
        
        {
            "question": "What is the largest continent by land area?",
            "options": ["A) Africa", "B) Asia", "C) Europe", "D) North America"],
            "answer": "B"
        },
        
        {
            "question": "Who discovered penicillin?",
            "options": ["A) Marie Curie", "B) Alexander Fleming", "C) Louis Pasteur", "D) Thomas Edison"],
            "answer": "B"
        }
    ]

    score = 0
    for i in range(10): 
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
    
    print(f"Your final score is {score} out of 10.")

while True:
    interactive_quiz()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing, Goodbye!")
        break   