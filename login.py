import bcrypt
import getpass

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
