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
        self.connection.execute("""
                                CREATE TABLE AdminAccount
                                ID INT PRIMARY KEY       NOT NULL,
                                USERNAME TEXT            NOT NULL,
                                PASSWORD PASSWORD        NOT NULL,
                                PASSWORDEXPIRYDATE  DATE NOT NULL,
                                FAILEDATTEMPTS INT       NOT NULL,
                                """)
        return
    

    def updateTable(listOfAdminAccounts):
        """ Updates the Admin table with an additional list of admins
        TO BE IMPLEMENTED
        """
        pass
    
    def findAdmin(self, userName, tableName):
        """ Searches for an admin user from their userName
        ParameterL: String Username  **Return: An admin Object if found or Null
        """
        self.connection.execute(f'SELECT {userName} FROM {tableName}')

    def getAllAdmins(self, tableName):
        """Returns all admins as a list of Objects of the type AdminAccount
        """
        return self.connection.execute(f'SELECT * FROM {tableName} ')


    def deleteTable(self, tableName):
        """Deletes the Intended tableName from the database
        Parameter: TableName,   **Return: Nothing
        """
        self.connection.execute(f'DELETE {tableName}')
        return
    
   
    """
    TODO(): Functionality to add in future updates Some SQL scrub means to 
    ensure that SQL injection is not possible through user inputs
    """  
        