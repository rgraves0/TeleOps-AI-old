import sqlite3

DB_NAME = "events.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            event_date TEXT,
            reminded INTEGER DEFAULT 0
        )
        '''
    )

    conn.commit()
    conn.close()

init_db()

def add_event(title, event_date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO events (title, event_date) VALUES (?, ?)",
        (title, event_date)
    )

    conn.commit()
    conn.close()

def list_events():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, event_date FROM events ORDER BY event_date ASC"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

def delete_event(event_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM events WHERE id = ?",
        (event_id,)
    )

    conn.commit()
    conn.close()

def get_due_events(today):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, event_date FROM events WHERE event_date = ? AND reminded = 0",
        (today,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

def mark_reminded(event_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE events SET reminded = 1 WHERE id = ?",
        (event_id,)
    )

    conn.commit()
    conn.close()
