import sqlite3

def fetch_data(app_name, trans_name):
    # Connect to SQLite database
    conn = sqlite3.connect('nfr_repository.db')
    cursor = conn.cursor()

    # Step 1: Fetch the most recent 5 distinct releaseID values
    cursor.execute("""
            SELECT DISTINCT releaseID
            FROM NFRDetails
            WHERE applicationName = ? AND transactionName LIKE ?
            ORDER BY releaseID DESC
            LIMIT 5
        """, (app_name, trans_name))
    release_ids = [row[0] for row in cursor.fetchall()]

    # Step 2: Construct dynamic SQL query
    select_clause = "SELECT applicationName, transactionName,"
    headers = ["applicationName", "transactionName"]

    # Add dynamic columns for SLA and TPS for each releaseID
    for release_id in release_ids:
        select_clause += f"""
           MAX(CASE WHEN releaseID = '{release_id}' THEN SLA END) AS '{release_id}_SLA',
           MAX(CASE WHEN releaseID = '{release_id}' THEN TPS END) AS '{release_id}_TPS',"""
        headers.append(f"{release_id}_SLA")
        headers.append(f"{release_id}_TPS")

    # Remove the trailing comma from the select clause
    select_clause = select_clause.rstrip(',')

    # Continue building the query with the WHERE clause
    query = f"""
    {select_clause}
    FROM NFRDetails
    WHERE applicationName = ? AND transactionName like ?
    GROUP BY applicationName, transactionName
    ORDER BY applicationName, transactionName;
    """

    # Print the generated query (optional)
    print("Generated Query:\n", query)

    # Execute the constructed query with parameters
    cursor.execute(query, (app_name, trans_name))

    # Fetch the results
    results = cursor.fetchall()

    # Print headers
    print("\t".join(headers))

    # Print the results
    for row in results:
        print("\t".join(map(str, row)))

    # Close connection
    conn.close()

# Example user input
application_name_input = "SVTM"
transaction_name_input = "%"

# Fetch and display data for the given inputs
fetch_data(application_name_input, transaction_name_input)
