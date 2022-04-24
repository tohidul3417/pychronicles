import random
import time

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "In which year was the University of Dhaka established?",
                "options": ["1910", "1921", "1947", "1952"],
                "correct_answer": "1921"
            },
            {
                "question": "Who was the first Vice-Chancellor of the University of Dhaka?",
                "options": ["Sir P.J. Hartog", "Dr. Muhammad Shahidullah", "Sir A.F. Rahman", "Dr. Ramesh Chandra Majumdar"],
                "correct_answer": "Sir P.J. Hartog"
            },
            {
                "question": "Which famous movement is closely associated with the University of Dhaka that later influenced the Bangladesh Liberation War?",
                "options": ["Non-Cooperation Movement", "Swadeshi Movement", "Language Movement", "Quit India Movement"],
                "correct_answer": "Language Movement"
            },
            {
                "question": "What is the nickname of the University of Dhaka?",
                "options": ["The Cambridge of the East", "The Oxford of the East", "The Harvard of Bangladesh", "The Pearl of Bengal"],
                "correct_answer": "The Oxford of the East"
            },
            {
                "question": "Which faculty was established first in the University of Dhaka?",
                "options": ["Faculty of Science", "Faculty of Arts", "Faculty of Law", "Faculty of Medicine"],
                "correct_answer": "Faculty of Arts"
            },
            {
                "question": "How many residential halls does the University of Dhaka currently have?",
                "options": ["11", "13", "19", "22"],
                "correct_answer": "19"
            },
            {
                "question": "Which prominent Bengali Nobel laureate was a student at the University of Dhaka?",
                "options": ["Rabindranath Tagore", "Amartya Sen", "Muhammad Yunus", "Kazi Nazrul Islam"],
                "correct_answer": "Muhammad Yunus"
            },
            {
                "question": "What is the approximate size of the University of Dhaka campus in acres?",
                "options": ["275", "600", "750", "900"],
                "correct_answer": "600"
            },
             {
                "question": "Who donated 600 acres of land for the establishment of the University of Dhaka?",
                "options": ["Nawab Khwaja Salimullah", "Lord Curzon", "Sir Khawaja Nazimuddin", "Sher-e-Bangla A.K. Fazlul Huq"],
                "correct_answer": "Nawab Khwaja Salimullah"
            },
            {
                "question": "What is the motto of the University of Dhaka?",
                "options": ["Education, Research, Progress", "Knowledge, Wisdom, Progress", "Education is light", "Advancement Through Knowledge"],
                "correct_answer": "Education is light"
            }
        ]
        self.score = 0
        self.total_questions = len(self.questions)
    
    def display_welcome(self):
        print("\n" + "=" * 60)
        print("\tUNIVERSITY OF DHAKA QUIZ CHALLENGE")
        print("=" * 60)
        print("\nTest your knowledge about Bangladesh's premier university!")
        print(f"You will be asked {self.total_questions} multiple-choice questions.")
        print("\nDid you know? The University of Dhaka, established in 1921,")
        print("played a significant role in the Bengali Language Movement")
        print("and later in the Bangladesh Liberation War.")
        print("\nLet's see how much you know about this historic institution!\n")
        input("Press Enter to start the quiz...")
        
    def shuffle_questions(self):
        random.shuffle(self.questions)
    
    def display_question(self, question_data, question_num):
        print("\n" + "-" * 60)
        print(f"Question {question_num}/{self.total_questions}: {question_data['question']}")
        
        # Create a shuffled copy of the options
        options = question_data['options'].copy()
        random.shuffle(options)
        
        # Display the options
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        # Get user's answer
        while True:
            try:
                user_choice = int(input("\nEnter your answer (1-4): "))
                if 1 <= user_choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        selected_answer = options[user_choice - 1]
        correct_answer = question_data['correct_answer']
        
        # Check if answer is correct
        if selected_answer == correct_answer:
            self.score += 1
            print("\n✓ Correct! Well done!")
        else:
            print(f"\n✗ Incorrect. The correct answer is: {correct_answer}")
        
        # Add interesting facts for some questions
        facts = {
            "1921": "The University of Dhaka was established on July 1, 1921, after the dissolution of the University of Calcutta's affiliation with institutions in East Bengal.",
            "Sir P.J. Hartog": "Philip Joseph Hartog served as the first Vice-Chancellor from 1920-1925 and helped establish many of the university's founding departments.",
            "Language Movement": "The 1952 Bengali Language Movement, largely led by Dhaka University students, was pivotal in establishing Bengali as an official language and later inspired the independence movement.",
            "The Oxford of the East": "This nickname reflects the university's academic excellence and historical significance in South Asia.",
            "19": "These residential halls accommodate thousands of students and have their own distinct cultures and traditions.", 
            "Nawab Khwaja Salimullah": "Nawab Khwaja Salimullah, the Nawab of Dhaka, was a major patron of education who generously donated the land that became the main campus of the University of Dhaka."
        }
        
        if correct_answer in facts:
            print(f"\nFact: {facts[correct_answer]}")
        
        time.sleep(1.5)  # Small pause to read the result
    
    def display_final_results(self):
        print("\n" + "=" * 60)
        print("\tQUIZ COMPLETED!")
        print("=" * 60)
        
        percentage = (self.score / self.total_questions) * 100
        
        print(f"\nYour final score: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        if percentage >= 80:
            print("Excellent! You're a true University of Dhaka expert!")
        elif percentage >= 60:
            print("Good work! You know quite a bit about the University of Dhaka.")
        elif percentage >= 40:
            print("Not bad! You have some knowledge about the University of Dhaka.")
        else:
            print("Keep learning! The University of Dhaka has a rich history worth exploring.")
    
    def run_quiz(self):
        self.display_welcome()
        self.shuffle_questions()
        
        for i, question in enumerate(self.questions, 1):
            self.display_question(question, i)
        
        self.display_final_results()
        
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again == "yes" or play_again == "y":
            self.__init__()  # Reset the game
            self.run_quiz()
        else:
            print("\nThank you for playing! Goodbye!")

if __name__ == "__main__":
    quiz = QuizGame()
    quiz.run_quiz()