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


# Run the login failed contion in a for loop

for attempt in range(6):
    if login(user,pw) == True:
        is_authenticated = True
        break

    else:
        print('Invalid username or password. Please try again')
        user = input('Enter Username: ')
        pw = input('Enter Password: ')

print('Login Successful' if is_authenticated == True else 'Sorry, your account has been locked due to too many failed attempts')



