from turtle import *
speed(0)

def tracer(l,n):
    l/=3
    if l<n:
        forward(n)
        left(45)
        forward(n)
        right(90)
        forward(n)
        left(45)   
        forward(n)
    else:
        tracer(l,n)
        left(45)
        tracer(l,n)
        right(90)
        tracer(l,n)
        left(45)   
        tracer(l,n)

def do(x,n):
    for i in range(3):
        tracer(x,n)
        right(120)
    done()
    
do(200,1)