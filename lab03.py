#This python file draws the initials NO.
#By Nick O'Dea, nicholas_odea@umail.ucsb.edu
#I hope to try pair programming in the near future.

import turtle
from math import *

#Beginning with seperate initials.
#My letter drawing functions assume nothing about turtle status.

def drawN(t, h, w):
    '''Draws the capital letter N, height h by width w.
       Uses the turtle t to draw the letter.
       Begins at the lower left of N.'''
    t.down()
    t.sety(t.ycor()+h)
    t.goto(t.xcor()+w, t.ycor()-h)
    t.sety(t.ycor()+h)
    t.up()

def drawO(t, h, w):
    '''Draws the capital letter O, height h by width w.
       Uses the turtle t to draw the letter.
       Begins at horizontal line at top of O.'''

    #Scaling factor sf ensures that sum of x,y components of the O's add to w,h
    
    sf = 0
    for i in range(1, 12):
        sf = sf + sin(pi/12*i)
    t.down()

    #Draws 24 sides
    #Uses trig functions to change angles between each side
    for i in range(0, 24):
        t.goto(t.xcor() + w*cos(pi/12*i)/sf , t.ycor() - h*sin(pi/12*i)/sf)

    t.up()

#A short function to make a space. 

def shiftSpace(t, s):
    '''Makes a space. For use between the two initials.'''
    t.up()
    t.setx(t.xcor()+s)

#A function that draws the pair of initials.

def drawNO(t, h, w, s):
    '''Draws the pair of initials NO using drawN(t,w,h) and
        drawO(t,w,h). The letters are drawn with turtle t, and are
        both of height h and width w. The turtle begins at the lower
        left of N, draws N. It then shifts a space s and draws O,
        beginning from the top-most line of O and ending at the top.'''

    
    #Since O starts at the middle-top, it could curve back and intersect N.
    #Thus, I have added another term to s such that when s=0, N and O are tangent.

    sf = 0
    for i in range(1, 12):
        sf = sf + sin(pi/12*i)
        
    drawN(t, h, w)
    shiftSpace(t, s+.5*w*(1-1/sf))
    drawO(t, h, w)

    #Moving turtle down to lower right of the O.
    t.down()
    shiftSpace(t,.5*w*(1+1/sf))
    t.sety(t.ycor()-h)
    

def go():
    '''Draws three pairs of initials. Begins by shifting a turtle nobert
        to the lower left, then draws initials of different
        widths, heights, and sizes.'''
    nobert = turtle.Turtle()
    nobert.up()
    
    #shifts Nobert and draws initials (x3)

    #height>width, smallest 
    nobert.goto(nobert.xcor()-250, nobert.ycor()-150)
    drawNO(nobert, 40, 10, 5)

    #width>height, medium size
    nobert.sety(nobert.ycor()-100)
    drawNO(nobert, 80, 200, 30)

    #similar width and height, largest 
    nobert.goto(nobert.xcor()-420, nobert.ycor()+200)
    drawNO(nobert, 200, 180, 40)

    


