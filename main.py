from turtle import Turtle, Screen
from process_guesses import ProcessGuesses
from process_data import ProcessData
from map_processing import MapProcessing
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("U.S States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

process_guesses = ProcessGuesses()
process_data = ProcessData()
map_processing = MapProcessing()
scoreboard = ScoreBoard()

# # To check the x and y coordination for US state name positions
# def get_x_y_coordination(x, y):
#     print(x, y)
# screen.onscreenclick(get_x_y_coordination)

correct_answers = process_guesses.correct_answers
game_is_on = True

while game_is_on:
    user_answer = process_guesses.answer_state()
    # print(f"USER_A_MAIN:  {user_answer}")

    if process_guesses.check_answer(user_answer, process_data.list_of_answers()):
        # if True, it needs to process the mapping
        scoreboard.increment_score()
        map_processing.markup_score()
        map_processing.markup_state(df_data=process_data.show_list(), answer=user_answer)
        # Update the previously marked states again to keep them displayed,
        # which disappear after a refresh(update)
        map_processing.update_previous_states(df_data=process_data.show_list(),
                                              answers_list=correct_answers)
        map_processing.message_to_user("You are correct!")
    elif user_answer in correct_answers:
        map_processing.message_to_user("You already got it earlier. Try a different state!")
    else:
        map_processing.message_to_user("You got it wrong... Try again!")

    if process_guesses.win_the_game():
        map_processing.message_to_user("You completed the game!")
        time.sleep(1)
        break

    if user_answer == "Exit":
        map_processing.message_to_user("Program ends...")
        time.sleep(1)
        break

    if user_answer is None:
        map_processing.message_to_user("Game canceled.")
        time.sleep(1)
        break

# placed this create_missing_states_csv outside the while loop
# so it creates a csv file whenever the game(loop) ends without anything affecting its conditions
process_data.create_missing_states_csv(correct_answers)









## Structure::
# 1. Main While Loop
# 2. Process_Guesses -- Check if right or wrong, Record correct guesses
# 3. Mark on the map -- Write correct answers on the map
# 4. Scoreboard
# 5. Database (process_data.py)
