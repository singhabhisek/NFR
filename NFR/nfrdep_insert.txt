import sqlite3
import datetime

# Establish SQLite connection
conn = sqlite3.connect('nfr_repository.db')
cur = conn.cursor()

# Ensure the table exists
cur.execute('''
CREATE TABLE IF NOT EXISTS NFROperationDependency (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    created_date DATETIME NOT NULL,
    modifiedBy TEXT,
    modifed_date DATETIME
)
''')

# Sample data
data = [
    ('OLB', '2023.1', 'Login Scenario', 'OLB_Login', 'Mule_Login', 'Sync', 'User login', 'No discrepancies', 'Details', 'admin', datetime.datetime.now(), None, None),
    ('OLB', '2024.5', 'Dashboard Access', 'OLB_Dashboard', 'Mule_Dashboard', 'Async', 'User accesses dashboard', 'No discrepancies', 'Details', 'admin', datetime.datetime.now(), None, None),
    ('SVTM', '2023.3', 'Transfer Funds', 'SVTM_Transfer', 'Mule_Transfer', 'Sync', 'Funds transfer', 'No discrepancies', 'Details', 'admin', datetime.datetime.now(), None, None),
    ('SVTM', '2024.2', 'View Transactions', 'SVTM_Transactions', None, None, 'Transaction viewing', 'No discrepancies', 'Details', 'admin', datetime.datetime.now(), None, None),
    ('Mule', '2024.M01', 'Generate Reports', 'Mule_Reports', None, None, 'Report generation', 'No discrepancies', 'Details', 'admin', datetime.datetime.now(), None, None),
    ('Mule', '2024.M01', 'Mule API Requests', 'Mule_APIRequests', 'OLB_APIRequests', 'Async', 'API request handling', 'No discrepancies', 'Details', 'admin', datetime.datetime.now(), None, None),
    ('Mobile', '2023.M03', 'Mobile Login', 'Mobile_Login', 'Mule_Login', 'Sync', 'Mobile login', 'No discrepancies', 'Details', 'admin', datetime.datetime.now(), None, None),
]

# Insert sample data
cur.executemany('''
INSERT INTO NFROperationDependency (applicationName, releaseID, businessScenario, transactionName, backendCall, callType, comments, discrepancyIndicator, additionalDetails, createdBy, created_date, modifiedBy, modifed_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', data)

# Commit changes and close connection
conn.commit()
conn.close()
