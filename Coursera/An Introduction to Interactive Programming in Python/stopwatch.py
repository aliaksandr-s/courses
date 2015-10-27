# template for "Stopwatch: The Game"
import simplegui
# define global variables

interval = 100 # timer interval = 0.1 sec
time = 0

succes_stop = 0
total_stop = 0

if_start = None # check if timer is running

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global m_sec
    m_sec = t%10; sec = t/10
    if sec >= 60:
        minute = sec / 60
        sec = sec % 60        
    else:
        minute = 0
    add_zero = ''
    if sec < 10: add_zero = '0'
    return str(minute) + ':'+ add_zero + str(sec) + '.' + str(m_sec)
    

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global if_start
    timer.start()
    if_start = True
    
    
    

def stop():
    global if_start
    global m_sec
    global total_stop
    global succes_stop
    timer.stop()
    
    if if_start:
        if m_sec == 0: succes_stop += 1
        total_stop += 1
    if_start = False
    

def reset():
    global time
    global total_stop
    global succes_stop
    timer.stop()
    time = 0
    total_stop = 0
    succes_stop = 0
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [140, 160], 50, "Yellow")
    canvas.draw_text(str(succes_stop) +'/'+ str(total_stop), [330, 30], 30, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 300)

# register event handlers

frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
start_button = frame.add_button('Start', start, 200)
stop_button = frame.add_button('Stop', stop, 200)
reset_button = frame.add_button('Reset', reset, 200)

# start frame
frame.start()


# Please remember to review the grading rubric