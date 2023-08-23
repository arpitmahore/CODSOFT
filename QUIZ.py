import tkinter as tk
from tkinter import messagebox
import random

# Define the quiz questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "What is the capital of Japan?": "Tokyo",
    "What is the capital of Australia?": "Canberra",
    # Add more questions and answers here
}

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.score = 0
        self.current_question = None

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=5)

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        self.answer_entry.delete(0, tk.END)

        if questions:
            self.current_question = random.choice(list(questions.keys()))
            self.question_label.config(text=self.current_question)
        else:
            self.show_final_score()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = questions.get(self.current_question)

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Wrong answer. The correct answer is {correct_answer}.")

        del questions[self.current_question]
        self.next_question()

    def show_final_score(self):
        messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour final score is: {self.score}")

def main():
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
