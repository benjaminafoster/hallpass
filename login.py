import bcrypt
import getpass
from termcolor import colored
from users import User
from database import insert_user, user_exists, get_user

# highest order function to handle logging in a user, returns username as string if successful
def login(username):
    if user_exists(username):
        record = get_user(username)
        stored_hash = record["password"] # type: ignore
        password = getpass.getpass("Enter password: ")
        user_bytes = password.encode('utf-8')
        if bcrypt.checkpw(user_bytes, stored_hash):
            print(colored("login successful!", 'green'))
            return username
    else:
        raise ValueError("login failed. check your password and try again")


# highest level function to handle registering a user in the HallPass db 'users' table
def register_user(username):
    if user_exists(username):
        raise Exception("user already exists")
    else:
        pw_hash = create_user_password()
        user = User(username, pw_hash)
        insert_user(user)

# interactive interface for securely creating a bcrypt-hashed password for user login
def create_user_password() -> bytes:
    password_hash = b''
    while True:
        first = getpass.getpass("Enter new password (text will not display): ").strip() # consider an input santization function for each type of input
        if first == "":
            print("You cannot create an empty password. Try again...")
            continue
        second = getpass.getpass("Confirm new password: ").strip()
        if first != second:
            print("Passwords did not match. Try again...")
        else:
            password_hash = get_bcrypt_password_hash(second)
            break
    return password_hash

# funtion that standardizes bcrypt hashed password creation
def get_bcrypt_password_hash(password:str) -> bytes:
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash

""" It is very important to remember that using bcrypt.checkpw requires just an
 encoded byte stream user input to check against the stored_hash.

stored_hash = get_bcrypt_password_hash("hello_world")

input = input("Enter password: ")
user_bytes = input.encode('utf-8')

print(bcrypt.checkpw(user_bytes, stored_hash))
"""

# Deprecated due to REPL functionality
def get_username() -> str: 
    valid_username = ""
    while True:
        user_input = input("Enter username: ")
        username = user_input.strip()
        if username == "":
            print("Username cannot be empty. Try again...")
        else:
            valid_username = username
            break
    return valid_username