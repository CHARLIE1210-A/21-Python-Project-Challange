# ================= QUESTIONS DATA =================
QUESTIONS = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["List", "Set", "Dictionary", "Tuple"],
        "answer": "Tuple"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": ["2", "3", "4", "Error"],
        "answer": "3"
    }
]

# ================= QUIZ LOGIC =================
def ask_question(question_data):
    print("\n" + question_data["question"])
    
    for idx, option in enumerate(question_data["options"], start=1):
        print(f"{idx}. {option}")
        
    while True:
        try:
            choice = int(input("\nSelect the correct option (1-4): "))
            if 1 <= choice <= 4:
                return question_data["options"][choice - 1]
            else:
                print("Invalid choice. Please select a number bwtween 1 to 4.")
                
        except ValueError:
            print("Invalid input. Please eneter a number.")
            
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def calculate_score(score, total):
    percentage = (score/total) * 100
    return percentage

# ================= MAIN QUIZ =================
def run_quiz():
    score = 0
    total_questions = len(QUESTIONS)
    
    print("Welcome to the Python Quiz!")
    
    for question_data in QUESTIONS:
        user_answer = ask_question(question_data)
        if check_answer(user_answer, question_data["answer"]):
            print("Correct, well done!")
            score  += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['answer']}")
            
    percentage = calculate_score(score, total_questions)
    
    print(f"\nQUIZ RESULTS: ")
    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {score}")
    print(f"Score Percentage: {percentage:.2f}%")
    
    if percentage >= 70:
        print("\nCongratulations! You passed the quiz.")
    else:
        print("\nBetter luck next time!, Try again to improve your score.")

# ================= ENTRY POINT =================
def main():
    while True:
        run_quiz()
        retry = input("Do you want to retake the quiz? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Thank you for playing the quiz! Goodbye!")
            break
        
if __name__ == "__main__":
    main()        
