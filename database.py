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
