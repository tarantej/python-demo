

from email import message
from xml.etree.ElementPath import get_parent_map

# Print Statement  - Use single quote('') or double quote("")
print("Hello, World");

# Triple quotes (""" """) - Prints statements as is

print("""Python is a programming language 
created by Guido van Rossum
He named the language after 
the british comedy group Monty Python""");

# Request user for input
# input - it a built in python prompt function. It brings the prompt function to the terminal and waits for the user input
# Variable - it is a container that can store a value we would want to use later in a program

# name = input("Type your name: ");

# Output the value of the variable name in a formatted string

# = - Assignment operator

# message = f"Hello, {name}!";
# print(message);

# Documentation string - For longer comments
"""
input - it a built in python prompt function. It brings the prompt function to the terminal and waits for the user input
"""

# Variables - We can create variables in Python by directly typing the name of the variable
# String literals - pre defined values that cannot be changed
# You cannot use a variable without declaring it
# We can assign new values to variables after declaring them
# Python variables must be lowercase, can use underscore (_) and must have a letter or underscore as its first variable character

first_name="Mark";
last_name="Zbikowski";

# Working with Numbers

score = 0; # Number Variable
score = "0"; # String Variable;Python lets us change the data type of the variable on the fly
score = 42,000,000; # is actually a tuple (database table record with 3 columns)

card_balance = -200; # We can even use negative numbers
total_price = 28.88; # Float values
neg_float = -.5 # Negative float numbers

# Arithematic Operations

a = 2;
b = 4;

c = a + b;
c = a - b;
c = a * b;
c = a / b;

# Multiple value operation - Multiplication and division take precedence over addition and subtraction

c = a + a * b - b;
print(c); # Answer will be 6

# Override precedence with parantheisis ()

c = (a + a) * b - b;
print(c); # Answer will be 12

# If there operations with the same precedance,python will set precedence from left to right

x = 8 / 4 / 2 # Answer will be 1; 8 divided by 4 is 2 and 2 divided by 2 is 1

# String Operations

part1 = "Stay Hungry";
part2 = "Stay Foolish";

# Concatenation

quote = part1 + part2;

# Formatted string literals

quote = f"{part1} {part2}"
print(quote);

# Pi example

pi = 3.14159265359
message = f"The number pi is apporximately equal to {pi}";
print(message);

# Adding format specifier

message = f"The number pi is apporximately equal to {pi:.2f}";
print(message);

# Character length

print(len(quote));

# Convert to uppercase / lowercase

message_up = quote.upper();
message_low = quote.lower();

# swap case String  - Convert uppercase to lower case and vice versa

message_swap = quote.swapcase();
print(message_swap);

# count - number of times a string occurs in a defined string

stay_count = quote.count("Stay");
print(stay_count);

# Boolean Data Type - is it True or False

is_empty = True; # Value is 1
is_hidden = False; # Value is 0

# Conditional Code

# If Else statement

balance = 5000;
cash = 100;

if balance > cash:
    balance -= cash
    print(f"Current balance is {balance}");
    print("Transaction complete")
else:
    print("Insufficient Balance");
    print(f"Current balance is {balance}");

# Code Block  - A section of code that gets executed together
# Python code must be indented or else you will get a syntax error
# Code block following the if condition must have a higher indentation than the if statement
# All code belonging to the same block must have the same indentation

# Comparison Operators

# > - greater than
# >=  greater than equal to
# < - less than
# <=  less than equal to
# ==  equal
# !=  not equal
# = - Assignment operator
# % - Modulus Operator - Calculates remainder of the division

# Elif - Else If

traffic_light = "Green";

if traffic_light == "Green":
    print("Go!")
elif traffic_light =="Yellow":
    print("Slow down and prepare to stop")
elif traffic_light =="Red":
    print("Stop")
elif traffic_light =="Blinking":
    print("Proceed with caution")
else:
    print("Invalid state");

# Logical Operators - and, or, not

# Functions - A named section of reusable code that performs a specific taskk

# Allow us to write code and reuse it anywhere withing the program

# Writing Functions

# Syntax

# def function_name(parameter1,parameter2........parameter_n):
#     # function body
#     return value;

# Function Naming Convention

# Function names are lowercase
# Words are seperated by underscore(_)
# Names should be descriptive
# Start function name with a verb

# Example  - Calculate Square area

# def calculate_square_area(side):
#     return side*side;

# # Calling the function

# area = calculate_square_area(5);

# print(area);

# Function Parameter Annotation - Inform the caller about the expected argument type

# def function_name(parameter1:expression, parameter2:expression):


# def calculate_square_area(side: int):
#     return side*side;

# Annotate function return type

# def function_name() -> return_type

# def calculate_square_area(side) -> int:
#     return side*side;

# Annotate default parameter values

# def function_name(parameter : expression = default_value):

# def calculate_square_area(side:int = 1):
#     return side*side;

# Calling the function

# area = calculate_square_area();
# print(area);

# Providing a value to the function parameter overrides the default argument

# area = calculate_square_area(10);
# print(area);

# Understanding scope of variables
# Local Scope - Variables defined within the function have a local scope. Python interprets this output seperately
# Global variables - Variables are declareed globally to be used outside of the function
# Avoid relying on global variables in functions

area = 0 # Global variable 

def calculate_square_area(side:int = 1) -> int:
    global area # use local variable area in a global scope outside of the function
    area = side*side; # local variable
    print(area);
    return area;

calculate_square_area(10)
print(area);