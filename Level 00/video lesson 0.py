from turtle import *


#we want to paint a house

#step 1: draw a square
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square



#drawing a door
forward(70)
color("yellow")
left(90)
forward(120)      #hight of the door
right(90)
forward(60)
right(90)
forward(120)
#end of the door

penup()
goto(200, 200)
pendown()

#start of the roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

exitonclick()