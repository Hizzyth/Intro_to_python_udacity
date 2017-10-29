import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward (100)
        some_turtle.right (90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle brad- Draws a square
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("blue")
    brad.speed (300)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)
    
    #create the turtle angie - Draw a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color ("black")
    angie.circle(100)
    #create the turtle tito- Draw a Triangle
    tito = turtle.Turtle()
    tito.shape("turtle")
    tito.color("white")
    y=0
    while y<3:
        tito.right(120)
        tito.forward(90)
        y=y+1
       
    turtle.exitonclick()

draw_art()
