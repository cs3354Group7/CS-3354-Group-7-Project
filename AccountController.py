# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:01:54 2022

@author: Kelvin Somtochukwu Ojiako
"""
import AdminAccount
import DatabaseController

class AccountController:
    
    def __init__(self):
        """Instantiates the Database and gets the necessary info ready"""
        self.databaseController =  DatabaseController()
        
    def validateLoginDetails(self, userName, password):
        """Verifies if the account exists and returns a boolean """
        adminResult = self.databaseController.findAdmin(userName)
        if adminResult is None or adminResult.password != password:
            return False
        else:
            return True
    
    def getAccount(self, userName):
         return self.databaseController.findAdmin(userName)
    
    def FinalTask(self):
        self.databaseController.disconnectFromDatabase()
        
    def saveAccount(self, newAccount):
        self.databaseController.saveAdminAccount(newAccount)
        
        
        
    def createNewAccount(self, userName, password, passWordExpiryDate, failedAttempts, priviledge):
        newAccount = AdminAccount(userName, password, passWordExpiryDate, failedAttempts, priviledge)
        self.databaseController.saveAdminAccount(newAccount)
    
