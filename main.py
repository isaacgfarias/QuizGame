from quiz_brain import Quiz
from questions_bank import QBank
from data import api as question_bank

bank = QBank()
quiz = Quiz(bank)

for d in question_bank['results']:
    bank.add_question(d['question'], d['correct_answer'])

quiz.begin()
