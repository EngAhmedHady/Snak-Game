#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:11:29 2019

@author: hady
"""
import IPython
app = IPython.Application.instance()
app.kernel.do_shutdown(True)  

import turtle
import time
import random

delay = 0.1

# Score
score = 0
HighScore = 0

# Setup the screen 
wn = turtle.Screen() #---------------Define a screen (can be any variable name)
wn.title("Snake Game By Hady")   # -------Window title
wn.bgcolor("DarkBlue")  # -----------Background color
wn.setup(width = 600, height= 600) #-Screen Dimension
wn.tracer(0) # ----------------------Turns off screen Update !!

# Snake Head
head = turtle.Turtle()
head.speed(0) #---!!!
head.shape("square") # --------------Draw the head of the snake as Square shape
head.color("yellow") # --------------Head Color
head.penup() # ----------------------Turtle Draw lines so by this line it will draw nothing-- !!!
head.goto(0,0) # --------------------Where the head is start (the center of the screen)
head.direction = "stop" #--------------usful later !!

# Snake Food
Food = turtle.Turtle()
Food.speed(0) #---!!!
Food.shape("circle") # --------------Draw the head of the snake as Square shape
Food.color("Lightgreen") # --------------Head Color
x = random.randint(10,200)
y = random.randint(10,200)
Food.penup() # ----------------------Turtle Draw lines so by this line it will draw nothing-- !!!
Food.goto(x,y) # --------------------Where the head is start (the center of the screen)
Food.direction = "stop" #--------------usful later !!

# Snake Tale segmants
Tail = []

# Functins

# === 5s Function to change head direction
def GoUp():
    if head.direction != "down":
        head.direction = "up"
def GoDown():
    if head.direction != "up":
        head.direction = "down"
def GoLeft():
    if head.direction != "right":
        head.direction = "left"
def GoRight():
    if head.direction != "left":
        head.direction = "right"
def Stop():
    head.direction = "stop"
# =========================================
    
def move():
    if head.direction == "up":
        if head.ycor() < 290 :
            y = head.ycor()  
            head.sety(y + 20)
        else:
            head.sety(-290)
        
        
    elif head.direction == "down":
        if head.ycor() > -290 :
           y = head.ycor() 
           head.sety(y - 20)
        else:
            head.sety(290)
        
        
    elif head.direction == "right":
        if head.xcor() < 290 :
          x = head.xcor() 
          head.setx(x + 20)
        else:
            head.setx(-290)
        
        
    elif head.direction == "left":
         if head.xcor() > -290 :
             x = head.xcor() 
             head.setx(x - 20)
         else:
            head.setx(290)
       


# key Binding
wn.listen() # # ----- to make it respond to keyboard hits 
wn.onkeypress(GoUp, "w") 
wn.onkeypress(GoDown, "s")
wn.onkeypress(GoLeft, "a")
wn.onkeypress(GoRight, "d")
wn.onkeypress(Stop, "h")

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0    High Score = 0   Game Speed: 0.1", align= "center", font=("Arial", 20, "normal"))

# Main the game loop
while True:
    
    wn.update() # ------------------Because wn.tracer stop update screen 
    
    if head.distance(Food) < 20:
        # Move the food to random position
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        Food.goto(x,y)
        #increase the score
        score += 10 
        
        # Challenge Speed
        if score > 0 and score % 100 == 0:
            delay -= 0.01 
        
        if score > HighScore:
            HighScore = score
        
        pen.clear()
        pen.write("score: {}    High Score: {}   Game Speed: {}".format(score, HighScore,round(delay,3)), align= "center", font=("Arial", 20, "normal"))
        
        # Segment growth
        NewSegment = turtle.Turtle()
        NewSegment.speed(0)
        NewSegment.shape("square")
        NewSegment.color("white")
        NewSegment.penup()
        Tail.append(NewSegment)
        
        
    for i in range(len(Tail)-1,0,-1):
        x = Tail[i-1].xcor()
        y = Tail[i-1].ycor()
        Tail[i].goto(x,y)
    if len(Tail)>0:
        x = head.xcor()
        y = head.ycor()
        Tail[0].goto(x,y)
      
        
    
    move() # -----------------------Call moving Function
    
    # check for Body collision
    for Segment in Tail:
        if Segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # Hide The Tail
            for j in Tail:
                j.goto(1000,1000)
          
            #Tail clear
            Tail.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("score: {}    High Score: {}   Game Speed: {}".format(score, HighScore,delay), align= "center", font=("Arial", 20, "normal"))

    
    time.sleep(delay)

wn.mainloop()
exit()
