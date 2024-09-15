import turtle
import random

# Constants
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10
DELAY = 125
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

#Global variables
snake =[]
snake_direction="up"
food_pos = (0, 0)
score = 0
player_name = ""

#Screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Sanake Game")
screen.bgcolor("white")
screen.setup(500,500)
screen.tracer(0)

#Pen
pen = turtle.Turtle("square")
pen.penup()
pen.pencolor("green")

#Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 10, FOOD_SIZE / 10)  # Set correct size
food.penup()

#Scoreboard
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.goto(0, HEIGHT / 2 - 40)
score_pen.hideturtle()

#Player name input
player_name = screen.textinput("Player Name", "Enter your name: ")

def reset():
    global snake, snake_direction, food_pos, score
    snake = [[0,0], [0,20], [0,40], [0,50], [0,60]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    score = 0
    update_scoreboard()
    move_snake()

def move_snake():
    global snake_direction, score

    # Next position for head of snake.
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_direction][0]
    new_head[1] = snake[-1][1] + offsets[snake_direction][1]

    # Check self-collision
    if new_head in snake[:-1]:
        game_over()
        return
    
    snake.append(new_head)

    if not food_collision():
        snake.pop(0)

    # Allow screen warping
    if snake[-1][0] > WIDTH / 2:
        snake[-1][0] -= WIDTH
    elif snake[-1][0] < - WIDTH / 2:
        snake[-1][0] += WIDTH
    elif snake[-1][1] > HEIGHT / 2:
        snake[-1][1] -= HEIGHT
    elif snake[-1][1] < -HEIGHT / 2:
        snake[-1][1] += HEIGHT
    
    #Clear previous snake stamps
    pen.clearstamps()

    # Draw snake
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    # Refresh screen
    screen.update()

    # Repeat
    turtle.ontimer(move_snake, DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        score += 1
        update_scoreboard()
        return True
    return False

def game_over():
    global score
    pen.goto(0, 0)
    pen.write("Game Over! {}'s Score: {}".format(player_name, score), align="center", font=("courier", 24, "normal"))
    #Drow replay button
    replay_button = turtle.Turtle()
    replay_button.penup()
    replay_button.color("blue")
    replay_button.goto(0, -40)
    replay_button.write("replay", align="center", font=("courier", 16, "normal"))
    replay_button.onclick(reset)

def update_scoreboard():
    score_pen.clear()
    score_pen.write("{}'s Score: {}".format(player_name, score), align="center", font=("courier", 16, "normal"))

def get_random_food_pos():
    x = random.randint(- int(WIDTH / 2) + FOOD_SIZE, int(WIDTH / 2) - FOOD_SIZE)
    y = random.randint(- int(HEIGHT / 2) + FOOD_SIZE, int(HEIGHT / 2) - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Let's go
reset()
turtle.done() 