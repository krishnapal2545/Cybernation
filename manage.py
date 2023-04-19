import sqlite3
from datetime import datetime

conn = sqlite3.connect('Cybernation.db')
cursor = conn.cursor()


class Database():

    def __init__(self):
        self.conn = sqlite3.connect('Cybernation.db')
        self.cursor = self.conn.cursor()

        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Fname           TEXT     NOT NULL,
        Lname           TEXT     NOT NULL,
        Gender          TEXT     NOT NULL,
        Org             TEXT     NOT NULL,
        Phone           INT      NOT NULL,
        Username        TEXT     NOT NULL,
        Password        TEXT     NOT NULL);''')

        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS Devices(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID         INTEGER  NOT NULL,
        Name           TEXT     NOT NULL,    
        IP             TEXT     NOT NULL   UNIQUE,
        Subnet         TEXT     NOT NULL,
        Description    TEXT     NOT NULL,
        Type           TEXT     NOT NULL,
        Username       TEXT     NOT NULL,
        Password       TEXT     NOT NULL,
        Enable         TEXT     NOT NULL,
        Device_Type    TEXT     NOT NULL  DEFAULT 'autodetect',
        Last_Modify    DATETIME NOT NULL);''')

        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS Configs(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DeviceID           TEXT     NOT NULL,
        Name               TEXT     NOT NULL,
        Config             TEXT     NOT NULL,
        Last_Modify        DATETIME NOT NULL);''')

    def saveUser(self, fname, lname, gen, org, phone, uname, passw):
        self.conn.execute('''
        INSERT INTO Users (Fname,Lname,Gender,Org,Phone,Username,Password) 
        VALUES(?,?,?,?,?,?,?)''', (fname, lname, gen, org, phone, uname, passw))
        self.conn.commit()

    def savedevice(self, data):
        self.conn.execute('''
        INSERT INTO Devices (UserID,Name,IP,Subnet,Description,Type,Username,Password,Enable,Last_Modify) 
        VALUES(?,?,?,?,?,?,?,?,?,?)''',
                          (str(data['userID']), str(data['Name']), str(data['IP']), str(data['Subnet']), str(data['Description']), str(data['Type']), str(data['Username']), str(data['Password']), str(data['Enable']), str(data['Last_Modify'])))
        self.conn.commit()

    def getAlldevice(self, user):
        self.cursor.execute(
            "SELECT * FROM Devices WHERE UserID = ?", (user[0],))
        return self.cursor.fetchall()

    def getdevice(self, IP):
        self.cursor.execute("SELECT * FROM Devices WHERE IP = ?", (IP,))
        return self.cursor.fetchone()

    def deleteDevice(self, IP):
        self.cursor.execute("DELETE FROM Devices WHERE IP = ?", (IP,))
        self.conn.commit()

    def saveconfig(self, config):
        self.conn.execute('''
        INSERT INTO Configs (DeviceID, Name, Config, Last_Modify) 
        VALUES(?,?,?,?)''', (str(config['deviceID']), str(config['Name']), str(config), str(config['Last_Modify']),))
        self.conn.execute('''
        UPDATE Devices SET Last_Modify = ? WHERE ID = ?''', (datetime.today(), str(config['deviceID']),))
        self.conn.commit()

    def getconfig(self, deviceID):
        self.cursor.execute("SELECT * FROM Configs WHERE DeviceID = ?", (deviceID,))
        return self.cursor.fetchall()


def savedevice(data):

    conn.execute('''
    CREATE TABLE IF NOT EXISTS Devices(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID         INTEGER  NOT NULL,
        Name           TEXT     NOT NULL,    
        IP             TEXT     NOT NULL   UNIQUE,
        Subnet         TEXT     NOT NULL,
        Description    TEXT     NOT NULL,
        Type           TEXT     NOT NULL,
        Username       TEXT     NOT NULL,
        Password       TEXT     NOT NULL,
        Enable         TEXT     NOT NULL,
        Device_Type    TEXT     NOT NULL  DEFAULT 'autodetect',
        Last_Modify    DATETIME NOT NULL);''')

    conn.execute('''
    INSERT INTO Devices (UserID,Name,IP,Subnet,Description,Type,Username,Password,Enable,Last_Modify) 
    VALUES(?,?,?,?,?,?,?,?,?,?)''',
                 (str(data['userID']), str(data['Name']), str(data['IP']), str(data['Subnet']), str(data['Description']), str(data['Type']), str(data['Username']), str(data['Password']), str(data['Enable']), str(data['Last_Modify'])))
    conn.commit()


def getAlldevice(user):
    cursor.execute("SELECT * FROM Devices WHERE UserID = ?", (user[0],))
    return cursor.fetchall()


def getdevice(IP):
    cursor.execute("SELECT * FROM Devices WHERE IP = ?", (IP,))
    return cursor.fetchone()


def deleteDevice(IP):
    cursor.execute("DELETE FROM Devices WHERE IP = ?", (IP,))
    conn.commit()


def saveUser(fname, lname, gen, org, phone, uname, passw):

    conn.execute('''
    CREATE TABLE IF NOT EXISTS Users(
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


def saveconfig(config):

    conn.execute('''
    CREATE TABLE IF NOT EXISTS Configs(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DeviceID           TEXT     NOT NULL,
        Name               TEXT     NOT NULL,
        Config             TEXT     NOT NULL,
        Last_Modify        DATETIME NOT NULL);''')
    conn.execute('''
    INSERT INTO Configs (DeviceID, Name, Config, Last_Modify) 
    VALUES(?,?,?,?)''', (str(config['deviceID']), str(config['Name']), str(config), str(config['Last_Modify']),))

    conn.execute('''
    UPDATE Devices SET Last_Modify = ? WHERE ID = ?''', (datetime.today(), str(config['deviceID']),))

    conn.commit()


def getconfig(deviceID):
    cursor.execute("SELECT * FROM Configs WHERE DeviceID = ?", (deviceID,))
    return cursor.fetchall()
