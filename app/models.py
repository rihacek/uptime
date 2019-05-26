from app import data
import json

class MyClass:
    x = 5
    stranger = "stranger"
    

class Dashboard: 
    def __init__(self):
        self.greeting = "Welcome to the dashboard!"
        
        __sysdao = data.SystemDAO()
        self.systems = __sysdao.getSystems()

class PingList:
    def __init__(self):
        __sysdao = data.SystemDAO()
        self.systems = __sysdao.getSystems()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)
