import pymysql
from app import config

#found a helper class at (https://medium.com/@vipinc.007/python-a-database-interaction-class-using-pymysql-3338fb90f38c)
class DBHelper:

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = config.MySQL.DBUSER
        self.password = config.MySQL.DBPASSWORD
        self.db = "uptime"

    def __connect__(self):
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.con.commit()
        self.__disconnect__()

class System:
    
    def __init__(self, systemData):
        self.systemID = systemData["ID"]
        self.systemName = systemData["Name"]
        self.description = systemData["Description"]
        self.parent = systemData["ParentID"] #refactor later to parent system object instead of reference
        self.address = systemData["Address"]
        self.pingtype = systemData["Type"]

class Response:
    
    def __init__(self, responseData):
        self.responseID = responseData["ID"]
        self.systemID = responseData["SystemID"]
        self.statusID = responseData["StatusID"] #todo: include lookup work in source query
        self.callTime = responseData["CallTime"]
        self.duration = responseData["Duration"]

class SystemDAO(object):
    __db = None;

    def __init__(self):
        self.__db = DBHelper()

    def getSystems(self):
        sql         = "select s.ID, s.Name, s.Description, s.ParentID, c.Type, c.Address "
        sql = sql   + "from uptime.System as s "
        sql = sql   + "inner join uptime.Connection as c "
        sql = sql   + "on s.ID = c.SystemID;"

        results = self.__db.fetch(sql)
        systems = []
        for i in results:
            systems.append(System(i))
        return systems

class ResponseDAO(object):
    __db = None;
        
    def __init__(self):
        self.__db = DBHelper()        

    def getResponse(self, thisID):
             
        sql = "select r.ID, r.SystemID, r.StatusID, r.CallTime, r.Duration "
        sql += "from uptime.Response as r "
        sql += "where r.ID = " + thisID + ";"

        results = self.__db.fetch(sql)
        responses = []
        for i in results:
            responses.append(Response(i))
        return responses

    def logResponse(self, sys, st, time, dur):

        sql = "insert into uptime.Response (`SystemID`,`StatusID`,`CallTime`,`Duration`) "
        #sql += f"values ({sys},{st},'{time}',{dur});"
        sql += "values ({},{},'{}',{});".format(sys, st, time, dur)
        self.__db.execute(sql)
        return "ok"