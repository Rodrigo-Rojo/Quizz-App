from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
GREEN = "#9bdeac"
RED = "#e7305b"


class ModelUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, text="Click to Start", width=280, fill="black", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        self.score_text = Label(text=f"Score: 0", font=("Courier", 13, "bold"), bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.is_true)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.is_false)

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.score_text.config(text=f"Score {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text, text="That was the last question, Happy with your score?")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(2000, self.get_next_question)
