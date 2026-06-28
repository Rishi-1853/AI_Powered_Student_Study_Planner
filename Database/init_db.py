import sqlite3

conn = sqlite3.connect(
    "Database/study_planner.db"
)

cursor = conn.cursor()

# USERS TABLE

cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL

)

""")

# STUDY HISTORY TABLE

cursor.execute("""

CREATE TABLE IF NOT EXISTS study_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    predicted_score REAL,

    study_plan TEXT,

    recommendations TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)

""")

conn.commit()

conn.close()

print(
    "Database Created Successfully"
)