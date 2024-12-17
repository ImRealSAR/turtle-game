import turtle as trtl

# Default turtle screen and setup before getting into program
screen = trtl.Screen()
screen.title("Tic Tac Toe")
screen.bgcolor("black")
screen_width = screen.window_width()
screen_height = screen.window_height()
screen.setup(width=screen_width, height=screen_height)

# basic turtle drawer
drawer = trtl.Turtle()
drawer.speed(0)
drawer.hideturtle()
font_setup = ("Arial", 32)

# vars
X_score = 0
O_score = 0
current_player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]

# Grid positions for reference
grid_positions = {
    (0, 0): (-200, 200), (0, 1): (0, 200), (0, 2): (200, 200),
    (1, 0): (-200, 0), (1, 1): (0, 0), (1, 2): (200, 0),
    (2, 0): (-200, -200), (2, 1): (0, -200), (2, 2): (200, -200)
}

# This shows our welcome/beginning game screen
def welcome_screen():
    screen.clear()
    screen.bgcolor("black")
    drawer.penup()
    drawer.goto(0, 100)
    drawer.color("white")
    drawer.write("Welcome to Tic Tac Toe!", align="center", font=font_setup)
    
    # Play Button
    draw_button(-100, 0, 200, 50, "green", "Play", start_game)
    # Toggle Light/Dark Mode
    draw_button(-150, -100, 300, 50, "blue", "Toggle Mode", toggle_mode)

def draw_button(x, y, width, height, color, text, action):
    drawer.goto(x, y)
    drawer.pendown()
    drawer.color("black", color)
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(width)
        drawer.left(90)
        drawer.forward(height)
        drawer.left(90)
    drawer.end_fill()
    drawer.penup()
    drawer.goto(x + width / 2, y + 10)
    drawer.color("white")
    drawer.write(text, align="center", font=("Arial", 20))
    screen.onclick(lambda a, b: action() if x < a < x + width and y < b < y + height else None)

# Logic to switch between dark/light mode
def toggle_mode():
    screen.bgcolor("white" if screen.bgcolor() == "black" else "black")
    welcome_screen()

def start_game():
    screen.clear()
    screen.bgcolor("black")
    draw_board()
    screen.onclick(game_click_handler)

def draw_board():
    drawer.color("white")
    for x in [-100, 100]:
        drawer.penup()
        drawer.goto(x, 300)
        drawer.pendown()
        drawer.goto(x, -300)
    for y in [100, -100]:
        drawer.penup()
        drawer.goto(-300, y)
        drawer.pendown()
        drawer.goto(300, y)

# Draw our "X" and "O" for the tic tac toe game
def draw_x(x, y):
    drawer.penup()
    drawer.goto(x - 40, y + 40)
    drawer.pendown()
    drawer.goto(x + 40, y - 40)
    drawer.penup()
    drawer.goto(x - 40, y - 40)
    drawer.pendown()
    drawer.goto(x + 40, y + 40)

def draw_o(x, y):
    drawer.penup()
    drawer.goto(x, y - 40)
    drawer.pendown()
    drawer.circle(40)

# Handle Clicks
def game_click_handler(x, y):
    global current_player
    for (row, col), (cx, cy) in grid_positions.items():
        if cx - 100 < x < cx + 100 and cy - 100 < y < cy + 100 and board[row][col] == '':
            board[row][col] = current_player
            draw_x(cx, cy) if current_player == 'X' else draw_o(cx, cy)
            current_player = 'O' if current_player == 'X' else 'X'
            winner = check_winner()
            if winner:
                drawer.penup()
                drawer.goto(0, 350)
                drawer.write(f"Player {winner} wins!", align="center", font=font_setup)
                screen.onclick(None)
            break

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '': return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '': return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '': return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '': return board[0][2]
    return None

# Start and run our game program
welcome_screen()
screen.mainloop()
