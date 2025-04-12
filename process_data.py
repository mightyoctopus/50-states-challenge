import pandas

DATA_FILE = "50_states.csv"

class ProcessData:
    def __init__(self):
        self.df = pandas.read_csv(DATA_FILE)

    def show_list(self):
        return self.df

    def list_of_answers(self):
        states_series = self.df.state
        return states_series.to_list()

    # def show_x_y_position(self):
    #     position = self.df[["x", "y"]]
    #     return position

    # match user answer with state in data
    # plus, it's good to process the x y coor task
    # right down here.
    def match_answer_to_row(self, data, user_answer):
        matching_row = data[data.state == user_answer]

        x_coordinate = matching_row["x"].values[0]
        y_coordinate = matching_row["y"].values[0]
        x_y_positions = (x_coordinate, y_coordinate)
        return x_y_positions

    def create_missing_states_csv(self, correct_answers):
        missing_states = []
        states_from_csv = self.df.state.to_list()

        for state in states_from_csv:
            if state not in correct_answers:
                missing_states.append(state)

        pandas.DataFrame(missing_states).to_csv("missing states.csv")



# test = ProcessData()
# print(test.compare_user_answers_to_csv_states(["Alabama", "texas", "florida", "north carolina"]))
