from app import data

#placeholder while exploring MVC re: python

class MyClass:
    x = 5
    stranger = "stranger"
    

class Dashboard: 

    def __init__(self):
        self.greeting = "Welcome to the dashboard!"
        
        __sysdao = data.SystemDAO()
        self.systems = __sysdao.getSystems()


