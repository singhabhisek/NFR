import sqlite3


def show_database_structure_and_values(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get a list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Iterate over all tables
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")

        # Get the schema of the table
        cursor.execute(f"PRAGMA table_info({table_name});")
        schema = cursor.fetchall()

        # Print the schema of the table
        print("Schema:")
        for column in schema:
            print(f"  {column[1]} ({column[2]})")

        # Get all rows from the table
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        # Print all rows
        print("Values:")
        for row in rows:
            print(f"  {row}")

    # Close the connection
    conn.close()


# Path to your SQLite database file
database_path = 'nfr_repository.db'

# Show database structure and values
show_database_structure_and_values(database_path)
