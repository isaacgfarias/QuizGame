from data import question_data
from question_model import Question


class QBank:

    def __init__(self):
        self.question_bank = []
        for q in question_data:
            question = Question(q["text"].replace('.', '?'), q["answer"])
            self.question_bank.append(question)

    def add_question(self, q_text: str, q_answer: str):
        self.question_bank.append(Question(q_text, q_answer))
