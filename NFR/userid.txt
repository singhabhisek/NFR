import sqlite3

# Initialize the SQLite database connection
conn = sqlite3.connect('nfr_repository.db')
cursor = conn.cursor()

# Create UserAccess table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS UserAccess (
        userid TEXT PRIMARY KEY,
        role TEXT,
        status TEXT
    )
''')

# Insert some initial data for testing
cursor.execute('''
    INSERT OR REPLACE INTO UserAccess (userid, role, status) 
    VALUES ('AS', 'admin', 'active'),
           ('poweruser1', 'poweruser', 'active'),
           ('user1', 'user', 'active')
''')

conn.commit()
conn.close()
