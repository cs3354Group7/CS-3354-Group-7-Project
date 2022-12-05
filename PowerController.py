# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:09:30 2022

@author: kso170000
"""

class PowerController:
    
    def __init__(self, vendingMachines, intendedState = False, schedule = None):
        #Initializes the database that stores schedule info and 
        
        self.intendedState = intendedState
        self.schedule = schedule
    
    
    def powerOff(self):
        self.intendedState = False
    
    def powerOn(self):
        self.intendedState = True
    
    

    