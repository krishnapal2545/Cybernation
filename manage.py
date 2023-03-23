
import sqlite3

conn = sqlite3.connect('Cybernation.db')
cursor = conn.cursor()

def savedevice(data):
    chk = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='Devices';")
    if not chk:
        conn.execute('''
        CREATE TABLE Devices(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            UserID         INTEGER  NOT NULL,
            Name           TEXT     NOT NULL,    
            IP             TEXT     NOT NULL UNIQUE,
            Subnet         TEXT     NOT NULL,
            Description    TEXT     NOT NULL,
            Type           TEXT     NOT NULL,
            Username       TEXT     NOT NULL,
            Password       TEXT     NOT NULL,
            Enable         TEXT     NOT NULL,
            Last_Modify    DATETIME NOT NULL);''')
        
    conn.execute('''
    INSERT INTO Devices (UserID,Name,IP,Subnet,Description,Type,Username,Password,Enable,Last_Modify) 
    VALUES(?,?,?,?,?,?,?,?,?,?)''',
    (str(data['userID']),str(data['Name']), str(data['IP']) , str(data['Subnet']), str(data['Description']), str(data['Type']), str(data['Username']), str(data['Password']), str(data['Enable']), str(data['Last_Modify'])))
    conn.commit()


def getAlldevice(user):
    cursor.execute("SELECT * FROM Devices WHERE UserID = ?",(user[0],))
    return cursor.fetchall()

def getdevice(IP):
    cursor.execute("SELECT * FROM Devices WHERE IP = ?",(IP,))
    return cursor.fetchone()

def deleteDevice(IP):
    cursor.execute("DELETE FROM Devices WHERE IP = ?",(IP,))
    conn.commit()

def saveUser(fname, lname, gen, org, phone, uname, passw):
    chk = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='Users';")
    if not chk:
        conn.execute('''
        CREATE TABLE Users(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Fname           TEXT     NOT NULL,
            Lname           TEXT     NOT NULL,
            Gender          TEXT     NOT NULL,
            Org             TEXT     NOT NULL,
            Phone           INT      NOT NULL,
            Username        TEXT     NOT NULL,
            Password        TEXT     NOT NULL);''')

    conn.execute('''
    INSERT INTO Users (Fname,Lname,Gender,Org,Phone,Username,Password) 
    VALUES(?,?,?,?,?,?,?)''',
                 (fname, lname, gen, org, phone, uname, passw))
    conn.commit()


