import webbrowser
import time
i = 0
print "Start at " + time.ctime()
while i<3:
	time.sleep(10) 
	webbrowser.open("https://www.youtube.com/watch?v=ktvTqknDobU")
	i+=1
	print "Take a break!"