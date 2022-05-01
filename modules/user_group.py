from json import loads

class User_group:
    def __init__(self,json_user_group,hostid):
        dic_user_group = loads(json_user_group)
        self.hostid = hostid
        self.gid = dic_user_group['gid']
        self.uid = dic_user_group['uid']

    def get_hostid(self):
        return self.hostid

    def get_gid(self):
        return self.gid

    def get_uid(self):
        return self.uid

    def set_hostid(self, hostid):
        self.hostid = hostid

    def set_gid(self,gid):
        self.gid = gid

    def set_uid(self,uid):
        self.uid = uid

    def get_dic(self):
        dic_session = {
            'hostid':self.hostid,
            'gid': self.gid,
            'uid': self.uid
        }
        return dic_session

