import tkinter as tk
from tkinter import messagebox

class ComputerQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Computer Quiz")
        self.master.geometry("400x300")
        self.master.configure(bg='#f0f0f0')

        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                "question": "What does CPU stand for?",
                "options": ["Central Processing Unit", "Central Process Unit", "Central Processor Unit", "Central Program Unit"],
                "correct": 0
            },
            {
                "question": "What does GPU stand for?",
                "options": ["Graphics Processing Unit", "General Processing Unit", "Graphical Processor Unit", "General Purpose Unit"],
                "correct": 0
            },
            {
                "question": "Which of the following is NOT a type of RAM?",
                "options": ["DRAM", "SRAM", "VRAM", "ROM"],
                "correct": 3
            },
            {
                "question": "What is the purpose of a PSU in a computer?",
                "options": ["It cools the CPU", "It provides power to the motherboard", "It stores data for the computer", "It controls the computer's display output"],
                "correct": 1
            },
            {
                "question": "Which of the following is the fastest type of storage?",
                "options": ["SSD", "HDD", "Optical Drive", "USB Flash Drive"],
                "correct": 0
            }
        ]

        self.create_widgets()

    def create_widgets(self):
        self.welcome_label = tk.Label(self.master, text="Welcome to my computer quiz!", font=("Arial", 16), bg='#f0f0f0')
        self.welcome_label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Start Quiz", command=self.start_quiz, font=("Arial", 12))
        self.start_button.pack()

    def start_quiz(self):
        self.welcome_label.pack_forget()
        self.start_button.pack_forget()

        self.question_label = tk.Label(self.master, text="", font=("Arial", 12), wraplength=380, bg='#f0f0f0')
        self.question_label.pack(pady=10)

        self.var = tk.IntVar()
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self.master, text="", variable=self.var, value=i, font=("Arial", 10), bg='#f0f0f0')
            button.pack(anchor='w', padx=20)
            self.option_buttons.append(button)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option)
            self.var.set(-1)  # Reset selection
        else:
            self.show_result()

    def check_answer(self):
        if self.var.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        if self.var.get() == self.questions[self.current_question]["correct"]:
            self.score += 1
        self.current_question += 1
        self.next_question()

    def show_result(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        result_label = tk.Label(self.master, text=f"Your final score is {self.score}/{len(self.questions)}.", font=("Arial", 16), bg='#f0f0f0')
        result_label.pack(pady=20)
        quit_button = tk.Button(self.master, text="Quit", command=self.master.quit, font=("Arial", 12))
        quit_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    quiz = ComputerQuiz(root)
    root.mainloop()


