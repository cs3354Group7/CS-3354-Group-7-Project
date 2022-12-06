# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 18:35:36 2022

@author: kso170000
"""


import sqlite3

class DatabaseController:
    defaultLocalDatabase = ""
    
    def __init__(self, dataBase = defaultLocalDatabase):
        """ Creates a new Connection between the database and Whatever other
        service needs access to persistence. If the database is None then it creates
        a local connection with a default DatabaseName and file path
        Parameter: Database URL  ** Return: Connection Object
        """
        if dataBase is not None:
            self.connection = sqlite3.connect(dataBase)
            self.databaseCursor = self.connection.cursor()
           
    
    
    def disconnectFromDatabase(self):
        """ Disconnects from the Database URL given.
        Parameter: Database URL  ** Return: Nothing
        """
        if self.connection is not None:
            self.connection.close()
        
        

    def createAdminAccountTable(self):
        """ Creates Admin Table corresponding to the AdminAccount Object
        Parameter: Database URL  ** Return: Nothing
        """
        self.databaseCursor.execute("""
                                CREATE TABLE AdminAccount
                                ID INT PRIMARY KEY       NOT NULL,
                                USERNAME TEXT            NOT NULL,
                                PASSWORD PASSWORD        NOT NULL,
                                PASSWORDEXPIRYDATE  DATE NOT NULL,
                                FAILEDATTEMPTS INT       NOT NULL,
                                PRIVILEDGE  INT          NOT NULL
                                """)
        return
    
    def saveAdminAccount(self, admin):
        t = (admin.userName, admin.password, admin.passWordExpiryDate, admin.failedAttempts, )
        self.databaseCursor.execute("""INSERT INTO AdminAccount (USERNAME, PASSWORD, PASSWORDEXPIRYDATE, FAILEDATTEMPTS, PRIVILEDGE)
                                    VALUES(? , ? , ? , ? , ?""", t)
        
    

    def updateTable(listOfAdminAccounts):
        """ Updates the Admin table with an additional list of admins
        TO BE IMPLEMENTED
        """
        pass
    
    def findAdmin(self, userName, tableName = "AdminAccount"):
        """ Searches for an admin user from their userName
        ParameterL: String Username  **Return: An admin Object if found or Null
        """
        self.databaseCursor.execute('SELECT ? FROM ?' (userName, tableName))

    def getAllAdmins(self, tableName = "AdminAccount"):
        """Returns all admins as a list of Objects of the type AdminAccount
        """
        return self.databaseCursor.execute('SELECT * FROM tableName', (tableName,))


    def deleteTable(self, tableName = "AdminAccount"):
        """Deletes the Intended tableName from the database
        Parameter: TableName,   **Return: Nothing
        """
        self.databaseCursor.execute('DELETE ?', (tableName, ))
        return
    
    def deleteAdmin(self, admin):
        self.databaseCursor.execute("DELETE FROM AdminAccount WHERE USERNAME = ?", (admin.userName,))
    
   
    """
    TODO(): Functionality to add in future updates Some SQL scrub means to 
    ensure that SQL injection is not possible through user inputs
    """  
        