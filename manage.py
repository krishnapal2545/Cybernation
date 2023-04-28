from datetime import *
import sqlite3


class Database:

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
        Activity           TEXT     NOT NULL,
        Last_Modify        DATETIME NOT NULL);''')

    def saveUser(self, fname, lname, gen, org, phone, uname, passw):
        self.conn.execute('''
        INSERT INTO Users (Fname,Lname,Gender,Org,Phone,Username,Password) 
        VALUES(?,?,?,?,?,?,?)''', (fname, lname, gen, org, phone, uname, passw))
        self.conn.commit()

    def getUser(self, uname, passw):
        self.cursor.execute(
            "SELECT * FROM Users WHERE Username = ? AND Password = ?", (uname, passw,))
        return self.cursor.fetchone()

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
        INSERT INTO Configs (DeviceID, Name, Config, Activity ,Last_Modify) 
        VALUES(?,?,?,?,?)''', (str(config['deviceID']), str(config['Name']), str(config['Destination']), str(config['Activity']), str(config['Last_Modify']),))
        self.conn.execute('''
        UPDATE Devices SET Last_Modify = ? WHERE ID = ?''', (datetime.today(), str(config['deviceID']),))
        self.conn.commit()

    def getconfig(self, deviceID):
        self.cursor.execute(
            "SELECT * FROM Configs WHERE DeviceID = ?", (deviceID,))
        return self.cursor.fetchall()

