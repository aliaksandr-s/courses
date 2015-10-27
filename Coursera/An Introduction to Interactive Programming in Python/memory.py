# implementation of card game - Memory

import simplegui
import random



# helper function to initialize globals
def new_game():    
    global deck, exposed, state, turns, first_ind, second_ind
    state = 0
    first_ind = None
    second_ind = None
    deck = range(0,8)*2
    random.shuffle(deck)
    exposed = [ False for n in deck]
    turns = 0
    label.set_text('Turns = ' + str(turns))
  
     
# define event handlers
def mouseclick(pos):
    global deck, state, first_ind, turns, second_ind
    # add game state logic here
    index = pos[0] // 50
    #print index, first_ind, second_ind
    if exposed[index] == False:
        if state == 0:
            first_ind = index
            exposed[first_ind] = True
            state += 1
        elif state == 1:
            second_ind = index
            exposed[second_ind] = True
            state += 1
            turns += 1
            label.set_text('Turns = ' + str(turns))
        elif state == 2:
            if deck[first_ind] != deck[second_ind]:
                exposed[first_ind] = False
                exposed[second_ind] = False
            exposed[index] = True
            first_ind = index
            state -= 1
        
    

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    # x helps to count the horyzontal place of number on canvas
    x = 0
    for i in range(len(deck)): 
        canvas.draw_text(str(deck[i]), (14 + x, 66), 50, "White")
        if exposed[i] == False:
            canvas.draw_polygon([[x, 0], [x + 50, 0], [x + 50, 100], [x, 100]], 1, "White", "Green")
        x += 50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric