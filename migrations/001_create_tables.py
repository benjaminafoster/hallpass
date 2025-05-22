import sys
import os
import sqlite_utils
migrations_dir = os.path.dirname(__file__)
sys.path.append(f'{migrations_dir}/..') # Appends project root to path IOT reference modules at the root

db = sqlite_utils.Database("../hallpass.db")

db.create_table(
    "users",
    columns={
        "user_id":int,
        "username":str,
        "password":bytes
    },
    pk="user_id",
    not_null={"user_id", "username", "password"},
    if_not_exists=True
)