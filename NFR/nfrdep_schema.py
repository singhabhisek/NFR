import sqlite3

# SQLite database file path
sqlite_db = 'nfr_repository.db'

# Connect to SQLite database
conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

# Create NFROperationDependency table
cursor.execute('''
    CREATE TABLE NFROperationDependency (
        Id INTEGER PRIMARY KEY,
        applicationName TEXT NOT NULL,
        releaseID TEXT NOT NULL,
        businessScenario TEXT NOT NULL,
        transactionName TEXT NOT NULL,
        backendCall TEXT,
        callType TEXT,
        comments TEXT,
        discrepancyIndicator TEXT,
        additionalDetails TEXT,
        createdBy TEXT NOT NULL,
        created_date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
        modifiedBy TEXT,
        modifed_date TEXT
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("SQLite database and table created successfully.")
