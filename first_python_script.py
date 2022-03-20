#hello.py -- First python code :)

# Variables
from lib2to3.pgen2.token import NEWLINE
from tkinter import N


msg = "Hello World"
print(msg)

# Input function
age = input("What is your age?")

#print variables with strings
print ("Ohh! Are you really " + (age) + "?")

birth_year = input("What is your birth year: ")

# int function
current_age = 2022 - int(birth_year)
print (current_age)