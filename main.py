#!/bin/python3

from turtle import *
from random import choice
import time 

screen = Screen()
screen.bgcolor('red')
penup()
hideturtle()
file = open("cards.txt", 'r')

def printCat(text):
  stats = cats[cat]
  clear()
  goto(0,80)
  shape(stats[3])
  setheading(90)
  stamp()
  setheading(-90)
  forward(135)
  style = ("Arial", 14, "bold")
  write (text, font=style, align="center" )
  forward(25)
  write ("Name: " + cat, font=style, align="center" )
  forward(25)
  write ("Intelligence: " + stats[0], font=style, align="center" )
  forward(25)
  write ("Age: " + stats[1], font=style, align="center" )
  forward(25)
  write ("Favorite Food: " + stats[2], font=style, align="center" )
  
cats = {}
for line in file.read().splitlines():
  name, intelligence, age, favfood, image = line.split(', ') 
  cats[name] = [intelligence, age, favfood, image]
  screen.register_shape(image)
file.close()

print ("You will choose a card, then the computer chooses a card")
print ("the intelligence of the cat will be added to your score")
print ("whoever has the highest score wins!!")
counter = 0
playerScore = 0
computerScore = 0
while counter < 3:
  cat = input('Choose a cat: (Choices are Scaredy, Kittycat, Blackie or r for random) ')
  if cat in cats:
    printCat("Players Choice")
    playerScore += int(cats[cat][0])
   
  elif cat == 'r':
    cat = choice(list(cats.keys()))
    playerScore += int(cats[cat][0])
    printCat("Players Choice")
    
  else:
    print("Cat doesn't exist")
  
    
  time.sleep(3)
  cat = choice(list(cats.keys()))
  computerScore += int(cats[cat][0])
  printCat('Computers Choice')
  
  
  counter +=1
  
print ("player score ", playerScore)
print ("computer score ", computerScore)  
if playerScore > computerScore:
  print ("You won!")
elif playerScore < computerScore:
  print ("You lost :(")
else:
  print ("Tie")