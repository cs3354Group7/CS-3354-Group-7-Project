# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:07:31 2022

@author: kso170000
"""

'''
The admin account class stores all the information about the admin.
It stores the username, password, password expiry date, and failed attempts.
The information about the admin account is able to be updated using the
updateAccount function. Though, if not all the information is being changed, 
there is the updatePassword and updateUsername functions to only change the
password of the username of the admin account. 
'''

class AdminAccount:
    def __init__(self, userName = None, password = None, passWordExpiryDate = None, failedAttempts = None, priviledge = None):
        self.userName = userName
        self.password = password
        self.passWordExpiryDate = passWordExpiryDate
        self.failedAttempts = failedAttempts
        self.priviledge = priviledge
        
    def updateAccount(self, admin):
        """ Updates Admin Account, like an alternate constructor 
        """
        if admin is not None :
            self.userName = admin.userName
            self.password = admin.passWord
            self.passWordExpiryDate = admin.passWordExpiryDate
            self.failedAttempts = admin.failedAttempts 
            self.priviledge = admin.priviledge
            
        
    def updatePassword(self, password):
       self.password = password
   
   
    def updateUserName(self, userName):
        self.userName = userName
    
    
    def updatePriviledge(self, priviledge):
        self.priviledge = priviledge
       
       
       
