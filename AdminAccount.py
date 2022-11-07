# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:07:31 2022

@author: kso170000
"""

class AdminAccount:
    def __init__(self, userName = None, password = None, passWordExpiryDate = None, failedAttempts = None):
        self.userName = userName
        self.password = password
        self.passWordExpiryDate = passWordExpiryDate
        self.failedAttempts = failedAttempts
        
    def updateAccount(self, admin):
        """ Updates Admin Account, like an alternate constructor 
        """
        if admin is None :
            print("Error! The updated field is invalid. Try Again...")
        else: 
            self.userName = admin.userName
            self.password = admin.passWord
            self.passWordExpiryDate = admin.passWordExpiryDate
            self.failedAttempts = admin.failedAttempts
        
    
    def updatePassword(self, password):
       self.password = password
   
   
    def updateUserName(self, userName):
        self.userName = userName
       
       
       