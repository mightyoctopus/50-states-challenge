from turtle import Turtle, Screen
from process_data import ProcessData
from process_guesses import ProcessGuesses
from scoreboard import ScoreBoard

class MapProcessing:
    def __init__(self):
        self.screen = Screen()
        self.turtle = Turtle()
        self.process_data = ProcessData()
        self.scoreboard = ScoreBoard()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(-20, 300)
        self.turtle.write(arg=f"Score: {self.scoreboard.score}", font=("Arial", 19, "normal"))
        # Separate turtle for messages to the user:
        # (for easier clear-ups)
        self.message_turtle = Turtle()
        self.message_turtle.hideturtle()
        self.message_turtle.penup()


    def markup_state(self, df_data, answer):
        if answer in df_data.state.values:
            # this needs the specific x, y coordinates
            # of the state of user input
            x_y_tuple = self.process_data.match_answer_to_row(df_data, answer)
            self.turtle.goto(x_y_tuple)
            self.turtle.write(answer, align="center", font=("Arial", 11, "normal"))

    # Display all the states from the correct answer list
    def update_previous_states(self, df_data, answers_list):
        for answer in answers_list:
            x_y_tuple = self.process_data.match_answer_to_row(df_data, answer)
            self.turtle.goto(x_y_tuple)
            self.turtle.write(answer, align="center", font=("Arial", 11, "normal"))

    def markup_score(self):
        self.turtle.clear()
        self.turtle.goto(-20, 300)
        self.turtle.write(arg=f"Score: {self.scoreboard.increment_score()}", font=("Arial", 19, "normal"))

    def message_to_user(self, msg):
        self.message_turtle.clear()
        self.message_turtle.goto(-80, -300)
        self.message_turtle.write(arg=f"{msg}", font=("Arial", 13, "normal"))

# test = MapProcessing()
# test.markup_state()



