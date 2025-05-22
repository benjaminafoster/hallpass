import bcrypt
import getpass
from users import User
from database import insert_user

def register_user():
    username = get_username()
    pw_hash = create_user_password()
    user = User(username, pw_hash)
    insert_user(user)

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

register_user()