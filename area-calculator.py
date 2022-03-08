# Calculate area of Square, Rectangle, Square

# Challenge

# Calculate Area of Rhombus
""" Area of Rhombus = p*q/2
    Create a function that takes in two parameters (p:float, q:float)
    Add option for Rhombus selection
    Add elif code block, calculate area and get_shape_name
"""

# Area of Square

from math import radians
from operator import le


def calculate_square_area(side:float):
    return side*side

# Area of Rectangle

def calculate_rectangle_area(length:float, breadth:float):
    return length*breadth

# Area of Circle

# Value of pi = 3.14 or 22/7

def calculate_circle_area(radius:float):
    pi=3.14
    return pi*(radius**2)

# Area of Rhombus

def calculate_rhombus_area(p:float, q:float):
    return (p*q)/2
    

# Ask user for input. input keyword for asking input from user. /t to indent a new tab

print("""
=================
Area Calculator
=================

Select a shape: 
""")

selection = input("""
\t 'S' - Square
\t 'R' - Rectangle
\t 'C' - Circle
\t 'Rh' - Rhombus

""")

# Using Condtional logic to calculate area of the shape


# Create a new function

def calculate_area(selection):

    area = 0

    if selection =='S':

        side = input("Enter the side: ")
        area = calculate_square_area(float(side))

    elif selection =='R':

        length = input("Enter the length: ")
        breadth = input("Enter breadth: ")
        area = calculate_rectangle_area(float(length),float(breadth))

    elif selection =='C':

        radius = input("Enter the radius: ")
        area = calculate_circle_area(float(radius))

    elif selection == 'Rh':
        p = input('Enter the value of p: ')
        q = input('Enter the value of q: ')
        area = calculate_rhombus_area(float(p), float(q))

    else:
        print("Invalid Selection")

    return area

# Create a function that gets input from the user

def get_shape_name(tag):

    shape = "Unknown"
    if tag == 'S':
        shape = 'Square'
    elif tag == 'R':
        shape = 'Rectangle'
    elif tag == 'C':
        shape = 'Circle'
    elif tag == 'Rh':
        shape = 'Rhombus'
    return shape

area = calculate_area(selection)

print(f"The area of {get_shape_name(selection)} the is {area}")



