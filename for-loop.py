# For-in Loop

# for var in sequence:
# Code block that runs 
# for each element in the sequence

from ast import Continue


for index in range(5):
    print(index)

# range is an inbuilt function that generates upto but not including the stop number

# range(start, stop, step) - start and step are optional parameters
# step - increments the number by the value specified

# While -  expression  runs till the condition ins true
# For - Runs for each element in the sequence

# Continue - skipe the rest of the code block and start excecuting the next right away

    if index % 2 == 0 : continue
    print(f"{index} - iteration count {index +1}")