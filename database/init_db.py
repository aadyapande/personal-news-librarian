import sqlite3
from pathlib import Path

DB_Path= Path(__file__).resolve().parent/"news_intel.db"
SCHEMA_PATH= Path(__file__).resolve().parent/"schema.sql"

def initialize_database():
    # to ensure that database directory exists
    DB_Path.parent.mkdir(parents=True, exist_ok=True)

    # connecting to SQLite DB
    conn = sqlite3.connect(DB_Path)
    cursor= conn.cursor()

    # enabling forgeign keys
    cursor.execute("PRAGMA foreign_keys= ON;")

    # load and execute the schema
    with open(SCHEMA_PATH,"r", encoding="utf-8") as f:
        schema_sql= f.read()
    
    cursor.executescript(schema_sql)

    conn.commit()
    conn.close()

    print(f"Database initialized at:{DB_Path}")


if __name__=="__main__":
    initialize_database()

    