class MainMenu:
    def __init__(self, machines, username, password):
        self.machines = machines
        self.username = username
        self.password = password

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