from json import loads

class Event:
    def __init__(self,json_event,hostid):
        dic_event = loads(json_event)
        self.hostid = hostid
        self.channel = dic_event['channel']
        self.data = dic_event['data']
        self.datetime = dic_event['datetime']
        self.eventid = dic_event['eventid']
        self.level = dic_event['level']
        self.pid = dic_event['pid']

    def get_hostid(self):
        return self.hostid

    def get_channel(self):
        return self.channel

    def get_data(self):
        return self.data

    def get_datetime(self):
        return self.datetime

    def get_eventid(self):
        return self.eventid

    def get_level(self):
        return self.level

    def get_pid(self):
        return self.pid

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_channel(self,channel):
        self.channel = channel

    def set_data(self,data):
        self.data = data

    def set_datetime(self,datetime):
        self.datatime = datetime

    def set_eventid(self,eventid):
        self.eventid = eventid

    def set_level(self,level):
        self.level =level

    def set_pid(self,pid):
        self.pid = pid

    def get_dic(self):
        dic_event = {
            'hostid': self.hostid,
            'channel': self.channel,
            'data': self.data,
            'datetime': self.datetime,
            'eventid': self.eventid,
            'level': self.level,
            'pid': self.pid,
        }
        return dic_event
