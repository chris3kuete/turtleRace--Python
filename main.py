from turtle import Turtle, Screen
import random

start_race = False

screen = Screen()
screen.setup(width=500, height=400)
person_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["blue", "orange", "yellow", "green", "purple", "brown"]
y_coordinates = [-70, -40, -10, 20, 50, 80]
turtle_names = []

for index in range(0, 6):
    turtle_new = Turtle(shape="turtle")
    turtle_new.penup()
    turtle_new.color(colors[index])
    turtle_new.goto(x=-230, y=y_coordinates[index])
    turtle_names.append(turtle_new)

if person_bet:
    start_race = True

while start_race:
    for turtle in turtle_names:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            start_race = False
            winner_color = turtle.pencolor()
            if winner_color == person_bet:
                print(f"you won!the {winner_color} is the winner")
            else:
                print(f"you lost!the {winner_color} is the winner")



screen.exitonclick()




screen.exitonclick()