# Lists

# Each element in a list has an index associated with it
# Index is zero based and increments with addition of new elements [0,1,2,3,4,5]

# list() creates an empty list. If we want to use it, we need to assign the return list to a variable
# list[index] returns the element along with its index

primes = list()

# Appending values to a list one at a time

primes.append(2)
primes.append(3)
primes.append(5)
primes.append(7)
primes.append(11)

print(primes)

# Appending multiple values to a list

primes= [2,3,5,7,11]

# The list mutable - Capable of changes

# Python allows mixing of multiple data types for creating lists

# insert - inserts a new element just before the element in the list at a given position, shifting the other values after index 1 to the right

primes.insert(1,13)

print(primes)

# pop - remove elements from the list

n = primes.pop(2) # Removes the element at index 2 and moves the rest of the elements to the left
print(primes)

n = primes.pop() # By default, pop removes the element at last index and moves the rest of the elements to the left
print(primes)

# removes - same as pop except that passing value argument is mandatory in order to use it

print(primes)

n = primes.remove(2) # Removes the element with value and moves the rest of the elements to the left

print(primes)