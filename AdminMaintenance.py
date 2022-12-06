# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 05:25:56 2022

@author: kso170000
"""

import AccountController
import Inventory
import PowerController
import Inventory

class AdminMaintenance:
    def __init__(self):
        self.accountController = AccountController()
        self.switch = PowerController()
        return
    
    def removeAdmin(self, admin):
        self.accountController.deleteAccount(admin)
        return
    
    def turnDeviceOff(self ):
        self.switch.powerOff()
        return
    
    def addNewAdmin(self, admin):
        self.accountController.createNewAccount(admin)
        
    def getInventory(self):
        self.accountController.getD
    
    def demoteAdmin():
        return
    
    def promoteAdmin():
        return 
    
    def suspendAdmin():
        return
    
    def checkDaysTillMaintenance():
        return
        