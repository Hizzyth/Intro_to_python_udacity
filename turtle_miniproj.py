import turtle

def draw_rohumbus(some_turtle):
    for i in range (1,5):
        some_turtle.forward (100)
        some_turtle.right (45)
        some_turtle.forward(100)
        some_turtle.right (135)

def draw_line(some_line):
    for i in range (1,2):
        some_line.right (90)
        some_line.forward (300)
        

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle brad- Draws a triangle
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("blue")
    brad.speed (1000)
    for i in range (1,37):
        draw_rohumbus(brad)
        brad.right(10)
    #Line
    for i in range (37,38):
        draw_line(brad)

    turtle.exitonclick()

draw_art()
