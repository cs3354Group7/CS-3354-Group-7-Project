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
        if dataBase is None:
            print("Error! Database URL was not given correctly. Try Connecting again.")
        else:
            print("creating Database Connection ......")
            
        self.connection = sqlite3.connect(dataBase)
    
    
    def disconnectFromDatabase(self):
        """ Disconnects from the Database URL given.
        Parameter: Database URL  ** Return: Nothing
        """
        if self.connection is None:
            print("No connection exists, Cannot Disconnect.")
        else: 
            self.connection.close()
            print("Successfully Disconnected")
        return
        

    def createAdminAccountTable():
        """ Creates Admin Table corresponding to the AdminAccount Object
        Parameter: Database URL  ** Return: Nothing
        """
        return
    

    def updateTable(listOfAdminAccounts):
        """ Updates the Admin table with an additional list of admins
        """
        return
    
    def findAdmin(userName):
        """ Searches for an admin user from their userName
        ParameterL: String Username  **Return: An admin Object if found or Null
        """
        pass

    def getAllAdmins(connection, tableName):
        """Returns all admins as a list of Objects of the type AdminAccount
        """
        return

    def deleteTable():
        """Deletes the Intended tableName from the database
        Parameter: TableName,   **Return: Nothing
        """
        return
    
   
    """
    TODO(): Functionality to add in future updates Some SQL scrub means to 
    ensure that SQL injection is not possible through user inputs
    """  
        