import random

# Define a list of questions and answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is 2 + 2?", "answer": "4"}
]

# Shuffle the questions to randomize the order
random.shuffle(questions)

# Initialize a variable to keep track of the score
score = 0

# Loop through the questions
for q in questions:
    # Display the question and wait for user input
    print(q["question"])
    user_answer = input("Your answer: ").strip()

    # Check if the user's answer is correct
    if user_answer.lower() == q["answer"].lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {q['answer']}\n")

# Display the final score
print(f"Your final score is: {score}/{len(questions)}")
