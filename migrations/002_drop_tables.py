import sys
import os
import sqlite_utils
migrations_dir = os.path.dirname(__file__)
sys.path.append(f'{migrations_dir}/..') # Appends project root to path IOT reference modules at the root

db = sqlite_utils.Database("../hallpass.db")

tables = db.table_names()

for table in tables:
    db.table(table).drop()