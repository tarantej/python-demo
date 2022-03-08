# Authenticate user credentials and return if the user is authenticated

def login(username: str, password: str) -> bool:
    is_authenticated = False
    if username == 'admin' and password == '1234':
        is_authenticated = True

    return is_authenticated

# Recieve input of username and password from the user

user = input('Enter Username: ')
pw = input('Enter Password: ')

# Account lock for too many login attempts - to break infinite loop

attempt = 1
max_attempts = 5

# Store value in another variable

# logged_in = login(user, pw)

# if logged_in:
#     message = 'Login Successful'
# else:
#     message = 'Invalid username or password. Please try again'

# print(message)

# A better way to do this - Conditional / Ternary Operators

# Conditonal Expression - Expression A (if condition)(else) Expression B

# print('Login Successful' if logged_in else 'Invalid username or password. Please try again')

# While loop - Tests a conditional expression and runs the body of the condtiion while the condtion remains true

"""
Syntax

while expression:
    # Code block that runs if expression is true
else: (optional)
    # If the expression is false
    # run this code and terminate the loop
"""
# Run the login failed contion in a while loop

while login (user, pw) == False:
# At every unsuccessful login, increase the number on attempts
    attempt += 1
# if the number of attempts is greater than the max attempts, break the loop and lock the account
    if attempt >= max_attempts: break
    print('Invalid username or password. Please try again')
    user = input('Enter Username: ')
    pw = input('Enter Password: ')
    
else:
    is_authenticated = True
    print('Login Successful')

if not is_authenticated:
    print('Sorry, your account has been locked due to too many failed attempts')



