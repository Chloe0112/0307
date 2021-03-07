import turtle

turtle.pensize(2)
turtle.pencolor("red")

for i in range(12):
    turtle.circle(120,30)
    turtle.right(30)
    turtle.pencolor('yellow')
    turtle.forward(80)

turtle.mainloop()

