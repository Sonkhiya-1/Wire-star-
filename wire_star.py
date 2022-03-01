from turtle import *
speed(20)
color('red')
bgcolor('black')
b = 200
c = 200
while b>0:
    left(b)
    forward(b*3)
    b = b-1
while c>0:
    right(c)
    forward(c*3)
    c = c-1