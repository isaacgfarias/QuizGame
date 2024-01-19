
class Question:

    def __init__(self, q_text: str, q_answer: str):
        self.question = q_text
        self.correct_answer = q_answer

    def get_text(self):
        return self.question

    def get_answer(self):
        return self.correct_answer
