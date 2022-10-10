import math
from tkinter import *
import tkinter
from PIL import Image
from moviepy.editor import *
import pygame

root = Tk()
root.title("Simple Calculator")
root.geometry('615x550')
root.configure(bg="white")

# Images
shirou_image = PhotoImage(file="C:\\Users\\Preston Williams\\Downloads\\Tkinter Simple Calculator\\Shirou.png")
ichigo_image = PhotoImage(file="C:\\Users\\Preston Williams\\Downloads\\Tkinter Simple Calculator\\ichigo.png")

# Sounds
shirou_theme = pygame.mixer.Sound("Shirou's Unlimited Blade Works Chant.mp3")
ichigo_theme = pygame.mixer.Sound("Ichigoat bankai sound effect.mp3")
voice = pygame.mixer.Channel(5)

# Define the buttons for Shirou and Ichigo
def play_shiroutheme():
    voice.play(shirou_theme) 

def play_ichigotheme():
    voice.play(ichigo_theme)

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=1, columnspan=3,)

# Define the operations the buttons do
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear_button():
    e.delete(0, END)

def add_button():
    first_number = e.get()
    global first_num
    global math
    math = "addition"
    first_num = int(first_number)
    e.delete(0, END)

def subtraction_button():
    first_number = e.get()
    global first_num
    global math
    math = "subtraction"
    first_num = int(first_number)
    e.delete(0, END)

def multiply_button():
    first_number = e.get()
    global first_num
    global math
    math = "multiplication"
    first_num = int(first_number)
    e.delete(0, END)

def divide_button():
    first_number = e.get()
    global first_num
    global math
    math = "division"
    first_num = int(first_number)
    e.delete(0, END)

def equal_button():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, first_num + int(second_num))
    elif math == "subtraction":
        e.insert(0, first_num - int(second_num))
    elif math == "multiplication":
        e.insert(0, first_num * int(second_num))
    else:
        e.insert(0, first_num / int(second_num))

# Define buttons
button_1 = Button(root, text="1", width=16, height=8, command=lambda: button_click(1), bg="#FFCCCB")
button_2 = Button(root, text="2", width=16, height=8, command=lambda: button_click(2), bg="#FFCCCB")
button_3 = Button(root, text="3", width=16, height=8, command=lambda: button_click(3), bg="#FFCCCB")
button_4 = Button(root, text="4", width=16, height=8, command=lambda: button_click(4), bg="#FFCCCB")
button_5 = Button(root, text="5", width=16, height=8, command=lambda: button_click(5), bg="#FFCCCB")
button_6 = Button(root, text="6", width=16, height=8, command=lambda: button_click(6), bg="#FFCCCB")
button_7 = Button(root, text="7", width=16, height=8, command=lambda: button_click(7), bg="#FFCCCB")
button_8 = Button(root, text="8", width=16, height=8, command=lambda: button_click(8), bg="#FFCCCB")
button_9 = Button(root, text="9", width=16, height=8, command=lambda: button_click(9), bg="#FFCCCB")
button_0 = Button(root, text="0", width=16, height=8, command=lambda: button_click(0), bg="#FFCCCB")
button_add = Button(root, text="+", width=16, height=8, command=add_button, bg="#FFCCCB")
button_subtract = Button(root, text="-", width=16, height=8, command=subtraction_button, bg="#FFCCCB")
button_multiply = Button(root, text="x", width=16, height=8, command=multiply_button, bg="#FFCCCB")
button_divide = Button(root, text="÷", width=16, height=8, command=divide_button, bg="#FFCCCB")
button_equal = Button(root, text="=", width=34, height=8, command=equal_button, bg="#FFCCCB")
button_clear = Button(root, text="CLEAR", width=34, height=8, command=clear_button, bg="#FFCCCB")
image_button1 = Button(root, image=shirou_image, width=120, height=120, command=play_shiroutheme, bg="#FFCCCB")
image_button2 = Button(root, image=ichigo_image, width=120, height=120, command=play_ichigotheme, bg="#FFCCCB")

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=1, column=4)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=2, column=4)

button_clear.grid(row=4, column=3, columnspan=2)
button_equal.grid(row=3, column=3, columnspan=2)

image_button1.grid(row=4, column=0)
image_button2.grid(row=4, column=2)

root.mainloop()