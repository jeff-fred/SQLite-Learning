# Learning to use SQLite3 for Python
# just the basics

''' File to add, check, and removes profiles through the pages.'''

import sqlite3



# ==== DataBase Attributes ====
databaseName = 'all_users.db'
tableName = "Users"
connection = sqlite3.connect(databaseName)
cursor = connection.cursor()
# =============================


# Create new Table if not yet created
def create_table():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS {0}(
            UserID INTEGER PRIMARY KEY,
            Username TEXT,
            Password TEXT)
        '''.format(tableName))
    connection.commit()
    
    # try:
    #     cursor.execute(
    #     '''
    #     CREATE TABLE {0}(
    #         IDnum INTEGER PRIMARY KEY,
    #         Username TEXT,
    #         Password TEXT,
    #     )
    #     '''.format(tableName))
    #     connection.commit()
    #     connection.close()
    # except sqlite3.OperationalError:
    #     None


# Add to the DataBase
def add_to_database(userID, userName, password):
    try:
        values = (userID, userName, password) # <---- Takes tuple in for input
        cursor.execute('''
            INSERT INTO {0}(UserID, Username, Password) VALUES(?,?,?)
            '''.format(tableName), (values))
        connection.commit()
    except sqlite3.IntegrityError:
        print("username already taken")

create_table()