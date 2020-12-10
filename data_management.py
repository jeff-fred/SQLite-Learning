# Learning to use SQLite3 for Python
# just the basics

''' File to add, check, and removes profiles through the pages.'''

import sqlite3
import tabulate



# ==== DataBase Attributes ====
databaseName = 'all_users.db'
tableName = "Users"
connection = sqlite3.connect(databaseName)
cursor = connection.cursor()
# =============================


# Create new Table if not yet created
def create_table():
    with connection:
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS {0}(
                UserID INTEGER PRIMARY KEY,
                Username TEXT,
                Password TEXT)
            '''.format(tableName))
        connection.commit()


# Display DataBase to console
def display_database():
    with connection:
        cursor.execute('SELECT * FROM Users')
        print(tabulate.tabulate(cursor.fetchall(), headers=['ID', 'Username', 'Password']))


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


# Remove from database
def remove_from_database(userID):
    with connection:
        cursor.execute('DELETE FROM Users WHERE UserID={0}'.format(userID))
        connection.commit()


# Create a new user ID number
def create_new_id():
    newId = 1
    with connection:
        cursor.execute('SELECT UserID FROM Users')
        connection.commit()
        allIds = [i[0] for i in cursor.fetchall()]

    for i in range(1, allIds[-1]):
        if i not in allIds:
            newId = i

    if newId in allIds:
        newId = allIds[-1]+1
            
    return newId

    