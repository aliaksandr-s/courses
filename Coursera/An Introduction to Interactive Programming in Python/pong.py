# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
Score1 = 0
Score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

paddle1_pos = HEIGHT / 2.0
paddle2_pos = HEIGHT / 2.0
paddle1_vel = 0
paddle2_vel = 0

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [(random.randrange(120, 240)/60.0), -(random.randrange(60, 180)/60.0)]
    else:
        ball_vel = [-(random.randrange(120, 240)/60.0), -(random.randrange(60, 180)/60.0)]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global Score1, Score2  # these are ints
    Score1 = 0
    Score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    global Score1, Score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #print ball_pos[1]
    
    # collide and reflect off of sides of canvas
    # 0 = x coordiante (horizon), 1 = y coordinate (verticle)
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    #spawn new ball if it touches the gutter
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] > paddle1_pos:
            spawn_ball(RIGHT)
            Score1 += 1
        elif ball_pos[1] < (paddle1_pos - PAD_HEIGHT):
            spawn_ball(RIGHT)
            Score1 += 1
        else:
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
    elif ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] > paddle2_pos:
            spawn_ball(RIGHT)
            Score2 += 1
        elif ball_pos[1] < (paddle2_pos - PAD_HEIGHT):
            spawn_ball(RIGHT)
            Score2 += 1
        else:
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen

    if paddle1_pos + paddle1_vel <= (PAD_HEIGHT - 1):
        paddle1_vel = 0
    elif paddle1_pos + paddle1_vel >= HEIGHT + 1:
        paddle1_vel = 0
    else:
        paddle1_pos += paddle1_vel
        
    # uncomment second player controls    
    """    
    if paddle2_pos + paddle2_vel <= (PAD_HEIGHT - 1):
        paddle2_vel = 0
    elif paddle2_pos + paddle2_vel >= HEIGHT + 1:
        paddle2_vel = 0
    else:
        paddle2_pos += paddle2_vel
    """
    paddle2_pos = ball_pos[1] + 10 # AI controls
        
    #print ball_pos[1]
    
    #print paddle2_pos
    
    # draw paddles
    canvas.draw_line([0 + HALF_PAD_WIDTH, paddle1_pos],[0 + HALF_PAD_WIDTH, paddle1_pos - PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos],[WIDTH - HALF_PAD_WIDTH, paddle2_pos - PAD_HEIGHT], PAD_WIDTH, "White")

    # draw scores
    canvas.draw_text(str(Score2), [150, 50], 30, "White")
    canvas.draw_text(str(Score1), [450, 50], 30, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5 #controls the speed of the paddles
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
        
    # uncomment second player controls    
    '''elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc'''

def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button("Restart", new_game)


# start frame
new_game()
frame.start()

 