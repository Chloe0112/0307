# import turtle
#
# turtle.pensize(5)
# turtle.pencolor("pink")
# turtle.fillcolor("lightskyblue")
#
# turtle.begin_fill()#准备填充
# for i in range(5):
#     turtle.forward(200)
#     turtle.right(144)
# turtle.end_fill()#完成填充
#
# turtle.mainloop()








# import turtle
#
# turtle.pensize(5)
# turtle.pencolor("black")
#
# for i in range(4):
#     turtle.left(90)
#     turtle.forward(100)
#
# turtle.left(45)
# turtle.forward(50)
# turtle.left(45)
# turtle.forward(100)
# turtle.left(135)
# turtle.forward(50)
#
# turtle.right(45)
# turtle.forward(100)
# turtle.right(135)
# turtle.forward(50)
# turtle.right(45)
# turtle.forward(100)
#
# turtle.mainloop()








# import turtle
# turtle.speed(1)
#
# def draw_tree(branch_length, t):
#     if branch_length >= 42:
#         t.forward(branch_length)
#         t.right(20)
#         draw_tree(branch_length-6, t)#回溯（递归）
#         t.left(40)
#         draw_tree(branch_length-6, t)
#         t.right(20)
#         t.backward(branch_length)
#
# turtle.left(90)
# turtle.up()#抬起尾巴
# turtle.backward(200)
# turtle.down()#放下尾巴
# draw_tree(66, turtle)
# turtle.color('white')
# turtle.forward(66)
#
# turtle.mainloop()

