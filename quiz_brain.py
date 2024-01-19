import random
from aux_functions import clear_console, valid_input


class Quiz:

    def __init__(self, bank) -> None:
        self.score: int = 0
        self.bank = bank
        self.questions: list = bank.question_bank

    def begin(self):
        clear_console()
        while True:
            cloned_questions = self.questions.copy()
            print(f'Welcome to Quiz Game!!!')
            for i in range(len(self.questions)):
                question = random.choice(cloned_questions)
                cloned_questions.remove(question)
                answer = valid_input(f'Q.{i+1}: ' + question.get_text() + '\n(True/False)\n', ['true', 'false'])
                if answer == question.get_answer().lower():
                    self.score += 1
                    clear_console()
                    print('Correct!\n')
                else:
                    clear_console()
                    print('Incorrect!\n')

            print(f'\nYour score is {self.score}/{len(self.questions)}')
            if valid_input('Play again? (y/n) ', ['y', 'n']) == 'n':
                break
            else:
                self.score = 0

