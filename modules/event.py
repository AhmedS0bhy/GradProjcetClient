from json import loads

class Event:
    def __init__(self,json_event,hostid):
        dic_event = loads(json_event)
        self.hostid = hostid
        self.logName = dic_event['logName']
        self.message = dic_event['message']
        self.TimeCreated = dic_event['TimeCreated']
        self.id = dic_event['id']
        self.level = dic_event['level']
        self.processId = dic_event['processId']
        self.machineName = dic_event['machineName']
    def get_hostid(self):
        return self.hostid

    def get_logName(self):
        return self.logName

    def get_message(self):
        return self.message

    def get_TimeCreated(self):
        return self.TimeCreated

    def get_id(self):
        return self.id

    def get_level(self):
        return self.level

    def get_processId(self):
        return self.processId

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_logName(self,logName):
        self.logName = logName

    def set_message(self,message):
        self.message = message

    def set_TimeCreated(self,TimeCreated):
        self.messagetime = TimeCreated

    def set_id(self,id):
        self.id = id

    def set_level(self,level):
        self.level =level

    def set_processId(self,processId):
        self.processId = processId

    def get_dic(self):
        dic_event = {
            'id': self.id,
            'machineName': self.machineName,
            'TimeCreated': self.TimeCreated,
            'logName': self.logName,
            'level': self.level,
            'processId': self.processId,
            'message': self.message,
            'hostid': self.hostid,
        }
        return dic_event
