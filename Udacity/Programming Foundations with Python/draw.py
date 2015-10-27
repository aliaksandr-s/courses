import turtle
import random
window = turtle.Screen()
window.bgcolor("white")

brad = turtle.Turtle()
brad.shape('square')
brad.speed(50)

andie = turtle.Turtle()
andie.shape('arrow')
andie.color('red')

def draw_square():
	while True:
					
		for x in range(1,5):	
			brad.forward(150)
			brad.right(90)
		brad.right(random.randint(1,15))
	def draw_circle(): 	
	 	andie.circle(50)


#draw_circle()
draw_square()
