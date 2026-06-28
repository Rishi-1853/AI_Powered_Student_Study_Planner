import sqlite3

DB_PATH = "Database/study_planner.db"


def save_history(
    user_id,
    predicted_score,
    study_plan,
    recommendations
):

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        """

        INSERT INTO study_history (

            user_id,

            predicted_score,

            study_plan,

            recommendations

        )

        VALUES (?, ?, ?, ?)

        """,

        (

            user_id,

            predicted_score,

            study_plan,

            recommendations

        )
    )

    conn.commit()

    conn.close()


def get_history(user_id):

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        """

        SELECT *

        FROM study_history

        WHERE user_id=?

        ORDER BY created_at DESC

        """,

        (user_id,)
    )

    records = cursor.fetchall()

    conn.close()

    return records

def register_user(
    username,
    email,
    password
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """

        INSERT INTO users(
            username,
            email,
            password
        )

        VALUES (?, ?, ?)

        """,

        (
            username,
            email,
            password
        )
    )

    conn.commit()
    conn.close()

def login_user(
    email,
    password
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT *

        FROM users

        WHERE email=?
        AND password=?

        """,

        (
            email,
            password
        )
    )

    user = cursor.fetchone()

    conn.close()

    return user