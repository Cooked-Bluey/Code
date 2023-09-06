import sqlite3
#The above code creates a SQLite database with multiple tables for managing employees, jobs,
#documents, teams, and main offices.
#:param cursor: The `cursor` parameter is an object that allows you to execute SQL queries and fetch
#results from the database. It is used to interact with the database and perform operations such as
#creating tables, inserting data, updating data, and querying data


def drop_tables(cursor):
    query = """
            DROP TABLE IF EXISTS CurrentDoc;
            DROP TABLE IF EXISTS Employee;
            DROP TABLE IF EXISTS Job;
            DROP TABLE IF EXISTS MainOffice;
            DROP TABLE IF EXISTS PastDoc;
            DROP TABLE IF EXISTS Team;
            """
    cursor.executescript(query)
    print('Drop tables if they exist')

    
    
def update_pragma(cursor):
    print("Update PRAGMA to support foreign keys")
    query = "PRAGMA foreign_keys = ON"
    cursor.execute(query)
    
def create_CurrentDoc_table(cursor):
    print("Create CurrentDoc Table")
    query = """CREATE TABLE CurrentDoc (
        CurrentDoc_id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL
        )"""
    cursor.execute(query)
    
def create_PastDoc_table(cursor):
    print("Create PastDoc Table")
    query = """CREATE TABLE PastDoc (
        PastDoc_id INTEGER PRIMARY KEY AUTOINCREMENT,
        text2 TEXT NOT NULL
        )"""
    cursor.execute(query)
    
def create_Employee_table(cursor):
    print("Create Employee Table")
    query = """CREATE TABLE Employee (
        Employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        First_Name TEXT NOT NULL,
        Last_Name TEXT NOT NULL,
        Phone INTEGER NOT NULL,
        Monday INTEGER,
        Tuesday INTEGER,
        Wednesday INTEGER,
        Thursday INTEGER,
        Friday INTEGER,
        Saturday INTEGER,
        Sunday INTEGER,
        Editing_staff_id
        )"""
    cursor.execute(query)
    
def create_MainOffice_table(cursor):
    print("Create MainOffice Table")
    query = """CREATE TABLE MainOffice (
        MainOffice_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Current_Client_First_Name TEXT NOT NULL,
        Current_Client_Last_Name TEXT NOT NULL,
        Potential_Jobs TEXT NOT NULL,
        PastDoc_id INTEGER NOT NULL,
        CurrentDoc_id INTEGER,
        FOREIGN KEY(CurrentDoc_id) REFERENCES CurrentDoc(CurrentDoc_id),
        FOREIGN KEY(PastDoc_id) REFERENCES PastDoc(PastDoc_id)
        )"""
    cursor.execute(query)
    
def create_Job_table(cursor):
    print("Create Job Table")
    query = """CREATE TABLE Job (
        Job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Cost INTEGER,
        Description TEXT NOT NULL,
        CurrentDoc_id INTEGER,
        MainOffice_id INTEGER,
        Team_id INTEGER,
        FOREIGN KEY (MainOffice_id) REFERENCES MainOffice (MainOffice_id),
        FOREIGN KEY (CurrentDoc_id) REFERENCES CurrentDoc (CurrentDoc_id),
        FOREIGN KEY (Team_id) REFERENCES Team (Team_id)
        )"""
    cursor.execute(query)
    

    
def create_Team_table(cursor):
    print("Create Team Table")
    query = """CREATE TABLE Team (
        Team_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Size INTEGER,
        Name TEXT NOT NULL,
        Description TEXT NOT NULL
        )"""
    cursor.execute(query)
    
def create_db(database_name):
    try:
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        
        drop_tables(cursor)
        update_pragma(cursor)

        create_CurrentDoc_table(cursor)
        create_PastDoc_table(cursor)
        create_Employee_table(cursor)
        create_Job_table(cursor)
        create_MainOffice_table(cursor)
        create_Team_table(cursor)
        
        connection.commit()
        connection.close()
        
        return "success"
    
    except Exception as e:
        print("Error: ", e)
        connection.rollback()
        connection.close()
        return "error"