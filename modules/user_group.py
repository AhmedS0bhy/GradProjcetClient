from json import loads

class User_group:
    def __init__(self,json_user_group,hostid):
        dic_user_group = loads(json_user_group)
        self.hostid = hostid
        self.gid = dic_user_group['gid']
        self.pid = dic_user_group['pid']

    def get_hostid(self):
        return self.hostid

    def get_gid(self):
        return self.gid

    def get_pid(self):
        return self.pid

    def set_hostid(self, hostid):
        self.hostid = hostid

    def set_gid(self,gid):
        self.gid = gid

    def set_pid(self,pid):
        self.pid = pid

    def get_dic(self):
        dic_session = {
            'hostid':self.hostid,
            'gid': self.gid,
            'pid': self.pid
        }
        return dic_session

