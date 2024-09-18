import turtle as t
t.speed('fastest')
t.pensize(3)

#1
t.color('OrangeRed4')
a = 250 * 3 ** (1/2)
t.fillcolor('OrangeRed4')
t.begin_fill()
for i in range(12):
    t.penup()
    t.goto(0, 0)
    t.forward(250)
    t.pendown()
    t.left(150)
    t.forward(a)
    t.left(120)
    t.forward(a)
    t.left(120)
    t.forward(a)
    t.right(20)
t.right(120)
t.end_fill()

#2
def draw_circles(outer_radius, inner_radius, num_circles):
    t.penup()  
    t.goto(0, -outer_radius)
    t.pendown() 
    t.circle(outer_radius)
    angle_step = 360 / num_circles

    for i in range(num_circles):
        t.penup()
        t.circle(outer_radius, angle_step)
        t.pendown()
        t.circle(inner_radius)
    t.end_fill()
outer_radius =220
inner_radius = 60
num_circles = 12
t.fillcolor('Yellow')
t.begin_fill()
draw_circles(outer_radius, inner_radius, num_circles)

#3
t.color('green4')
t.teleport(0,0)
t.fillcolor('green4')
t.begin_fill()
for i in range(24):   
    t.circle(60)
    t.right(15)
t.end_fill()

#4
t.color('Orange3')
t.teleport(0,0)
t.begin_fill()
for i in range(12):
    t.fillcolor('Orange1')
    t.circle(120)
    t.right(30)
t.end_fill()

#5
t.color('orange')
t.teleport(0,0)
t.begin_fill()
for i in range(12):
    t.fillcolor('yellow')
    t.circle(45)
    t.right(30)
t.end_fill()

for i in [10]:  
    t.begin_fill()
    t.fillcolor('RED4')  
    t.penup()
    t.goto(0, -i)
    t.pendown()
    t.circle(i)
    t.end_fill()



t.hideturtle()
t.done()
