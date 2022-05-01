from json import loads

class Session:
    def __init__(self,json_session,hostid):
        dic_session = loads(json_session)
        self.hostid = hostid
        #host, pid, registry_hive, time, type, user
        self.host = dic_session['host']
        self.pid = dic_session['pid']
        self.registry_hive = dic_session['registry_hive']
        self.time = dic_session['time']
        self.type = dic_session['type']
        self.user = dic_session['user']

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_host(self,host):
        self.host - host

    def set_pid(self,pid):
        self.pid = pid

    def set_registry_hive(self,hive):
        self.registry_hive = hive

    def set_time(self,time):
        self.time = time

    def set_type(self,type):
        self.type = type

    def set_user(self,user):
        self.user = user

    def get_hostid(self):
        return self.hostid

    def get_host(self):
        return self.host

    def get_pid(self):
        return self.pid

    def get_registry_hive(self):
        return self.registry_hive

    def get_time(self):
        return self.time

    def get_type(self):
        return self.type

    def get_user(self):
        return self.user

    def get_dic(self):
        dic_session = {
            'hostid': self.hostid,
            'host': self.host,
            'pid': self.pid,
            'registry_hive': self.registry_hive,
            'time': self.time,
            'type':self.type,
            'user':self.user,
        }
        return dic_session

