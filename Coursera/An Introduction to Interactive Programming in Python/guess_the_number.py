
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random




# helper function to start and restart the game
"""def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, 100)
    #print secret_number
    """


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global i, v
    i, v = 7, 7
    secret_number = random.randrange(0, 100)
    #print secret_number
    print """I thought the number in range: 0-100.
Try to guess it. 
You have:""",i, "attempts"

    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global i, v
    i,v = 10, 10
    secret_number = random.randrange(0, 1000)
    #print secret_number    
    print """I thought the number in range: 0-1000.
Try to guess it. 
You have:""",i, "attempts"
    
    
def input_guess(guess):
    global i
    
    guess = int(guess)
    i -= 1
    print "Guess was", guess     
    if guess > secret_number:
        print "Lower"
    elif guess < secret_number:
        print "Higher"
    else:
        print "Correct!",guess, "is the right answer! Let's play again"
        if v == 7: range100()
        if v == 10: range1000()
        
    # lose checker and restart
    print i, "Attempts left"
    if i == 0: 
        print  "You Lose. Let's try again." 
        if v == 7: range100()
        if v == 10: range1000()
    
    
    
    
# create frame
frame = simplegui.create_frame('Testing', 300, 150)
inp = frame.add_input('Guess the number', input_guess, 100)
frame.add_button('Range: 0-100', range100, 150)
frame.add_button('Range: 0-1000', range1000, 150)
# register event handlers for control elements and start frame


# call new_game 
range100()


