#importing necessary modules
import tkinter
import pygame
import os

#asks user for name so it can be used in naming the window
g = input("Hello! What is your name? ")

#greets the user through a for loop
for item in g:
  print("Hi!")
  break

#listing files in directory where music will be located
r = os.listdir()

#user input to find name of mp3
i = input("Type the name of the song you wish to play. ").lower() + ".mp3"

#if i is not in the directory and is not the string 'quit', the function quits out
def start():
  if i not in r:
    print("Invalid Input.")
    quit()
  elif i == "quit":
    quit()

#calls start, initializes tkinter for graphical interface, creates title of window, and initializes pygame and mixer
start()
root = tkinter.Tk()
root.title(g + "'s Music Player")
pygame.init()
pygame.mixer.init()

#function with parameter
def m(i):
  pygame.mixer.music.load(i) 

#functions to play, pause, stop, resume songs
def playsong():
  print("Currently Playing: " + i)
  m(i)
  pygame.mixer.music.play()
def stopsong():
  print("Stopped: " + i)
  pygame.mixer.music.stop()
def pausesong():
  print("Paused: " + i)
  pygame.mixer.music.pause()
def resumesong():
  print("Resumed: " + i)
  pygame.mixer.music.unpause()

#function to quit in case of an invalid input or request to quit
def quit():
  root.destroy()

#creates buttons that execute functions above
tkinter.Button(root,text="play",command=playsong).grid(row=1,column=0)
tkinter.Button(root,text="stop",command=stopsong).grid(row=1,column=1)
tkinter.Button(root,text="pause",command=pausesong).grid(row=1,column=2)
tkinter.Button(root,text="resume",command=resumesong).grid(row=1,column=3)

#creates loop for tkinter, allowing the user to see the buttons
tkinter.mainloop()