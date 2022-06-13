import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
turtle.shape(image)
# screen.bgpic(image)
correct_guesses = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name").title()
    if answer_state in all_states:
        x_cor = data[data["state"] == answer_state].x
        y_cor = data[data["state"] == answer_state].y
        timmy.goto(int(x_cor), int(y_cor))
        timmy.write(answer_state)
        correct_guesses.append(answer_state)
    if answer_state == "Exit":
        missing_list = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_list)
        new_data.to_csv("states_to_learn")
        break
