'''
The Main Menu class stores the username, password and the machines
viewable by the current user. The browseMachines function returns 
all the vending mechines viewable by the user and the searchMachines
function returns the specific machine the user is searching for. 
The login function decides whether or not the user has the ability to login
by giving the user an access or denial token. The logout function revokes the
current user's session. 
'''

import AccountController

class MainMenu:
    def __init__(self, machines, username, password):
        self.machines = machines
        self.username = username
        self.password = password
        self.accountController = AccountController()

    def browseMachines(self):
        return self.machines

    def searchMachines(self, machineLookup):
        for machine in self.machines:
            if machine == machineLookup:
                return machine

    def login(self):
        for user in DatabaseManager.loginInfo:
            if user == self.username:
                if DatabaseManager.loginInfo[user] == self.password:
                    return accessToken
        return denialToken

    def logout(self):
        self.username = ""
        self.password = ""
