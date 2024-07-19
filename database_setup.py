# database_setup.py
import sqlite3

def setup_database():
    connection = sqlite3.connect('lifecycle.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CycleConnects (
        id INTEGER PRIMARY KEY,
        start TEXT,
        end TEXT,
        type TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS LifeCycle (
        stage TEXT PRIMARY KEY,
        stagedesc TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SubStage (
        substagename TEXT,
        substagedesc TEXT,
        exemplar TEXT,
        stage TEXT,
        FOREIGN KEY (stage) REFERENCES LifeCycle(stage)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tools (
        ToolName TEXT,
        ToolDesc TEXT,
        ToolLink TEXT,
        ToolProvider TEXT,
        stage TEXT,
        FOREIGN KEY (stage) REFERENCES LifeCycle(stage)
    )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    setup_database()
