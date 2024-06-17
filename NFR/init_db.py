import sqlite3

connection = sqlite3.connect('nfr_repository.db')

with connection:
    # connection.execute('''CREATE TABLE IF NOT EXISTS NFRDetails (
    #                         Id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                         applicationName TEXT NOT NULL,
    #                         releaseID TEXT NOT NULL,
    #                         businessScenario TEXT NOT NULL,
    #                         transactionName TEXT NOT NULL,
    #                         SLA REAL,
    #                         TPS REAL,
    #                         backendCall TEXT,
    #                         callType TEXT,
    #                         comments TEXT,
    #                         discrepancyIndicator TEXT,
    #                         additionalDetails TEXT,
    #                         createdBy TEXT NOT NULL,
    #                         created_date TEXT DEFAULT (datetime('now')),
    #                         modifiedBy TEXT,
    #                         modified_date TEXT
    #                     );''')

    connection.execute('''INSERT INTO NFRDetails (applicationName, releaseID, businessScenario, transactionName, SLA, TPS, createdBy)
                          VALUES ('App4', 'Release3', 'Scenario04', 'Login', 5, 100, 'user1'),
                           ('App4', 'Release3', 'Scenario04', 'LogOff', 5, 100, 'user1'),
                            ('App4', 'Release3', 'Scenario04', 'Dashboard', 5, 100, 'user1'),
                            ('App5', 'Release1', 'Scenario04', 'AccountDetails', 15, 10, 'user1'),
                             ('App5', 'Release1', 'Scenario06', 'Login', 5, 12, 'user1'),
                                 ('App6', 'Release2', 'Scenario04', 'Login', 4, 10, 'user1');''')

print("Database initialized with sample data.")
