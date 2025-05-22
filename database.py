import sqlite_utils
from constants import DB_FILENAME
from users import User

# ORM-assisted query to insert a new user into the 'users' database
def insert_user(user:User):
    db = sqlite_utils.Database(DB_FILENAME)
    db["users"].insert({ # type: ignore
        "username":user.username,
        "password":user.password
    })

# function that checks if a user already exists in the database
def user_exists(username:str) -> bool:
    if get_user(username):
        return True
    return False

# funciton that queries the database for user based on username
def get_user(username:str):
    db = sqlite_utils.Database(DB_FILENAME)
    result = db.query(f'SELECT * FROM users where username=?', [username])
    results_list = list(result)
    if results_list:
        record = results_list[0]
        return record
    else:
        return None