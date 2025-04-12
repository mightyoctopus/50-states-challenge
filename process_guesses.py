from turtle import Turtle, Screen
import pandas

class ProcessGuesses:
    def __init__(self):
        self.screen = Screen()
        self.pandas = pandas
        self.correct_answers = []

    def answer_state(self):
        answer = self.screen.textinput(title=f"{len(self.correct_answers)}/50 States Correct", prompt="What's another state's name?")
        # print("USER ANSWER:" + " " + answer)
        if answer is None:
            return None # None returned when Cancel button was clicked
        return answer.title()

    def check_answer(self, user_answer, answer_list_data):
        if user_answer in answer_list_data:
            if not user_answer in self.correct_answers:
                self.correct_answers.append(user_answer)
                return True
        else:
            return False

    def win_the_game(self):
        return len(self.correct_answers) == 50




# test = ProcessGuesses
# print(test.answer_state())

