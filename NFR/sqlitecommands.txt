import sqlite3


def execute_sql(db_path, sql):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Execute the SQL statement
        cursor.execute(sql)
        conn.commit()
        print("SQL executed successfully.")

        # If the SQL is a SELECT statement, fetch and display results
        if sql.strip().lower().startswith("select"):
            results = cursor.fetchall()
            for row in results:
                print(row)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        conn.close()


# Example usage
if __name__ == "__main__":
    # Path to your SQLite database file
    database_path = 'nfr_repository.db'

    # Example SQL statements
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    );
    """

    alter_table_sql = """
    ALTER TABLE users ADD COLUMN email TEXT;
    """

    insert_sql = """
    INSERT INTO users (name, age, email) VALUES ('Alice', 30, 'alice@example.com');
    """

    update_sql = """
    UPDATE users SET age = 31 WHERE name = 'Alice';
    """

    delete_sql = """
    DELETE FROM users WHERE name = 'Alice';
    """

    drop_table_sql = """
    DROP TABLE IF EXISTS users;
    """

    # Execute the SQL statements
    print("Creating table...")
    execute_sql(database_path, create_table_sql)

    print("\nAltering table...")
    execute_sql(database_path, alter_table_sql)

    print("\nInserting data...")
    execute_sql(database_path, insert_sql)

    print("\nUpdating data...")
    execute_sql(database_path, update_sql)

    print("\nDeleting data...")
    execute_sql(database_path, delete_sql)

    print("\nDropping table...")
    execute_sql(database_path, drop_table_sql)
