import os

PROJECT_ROOT = os.getcwd()

DB_FILENAME = "hallpass.db"
DB_ABS_PATH = os.path.join(PROJECT_ROOT, DB_FILENAME) # required

print(DB_ABS_PATH)
