from json import loads
class User:
    def __init__(self,json_user,hostid):
        dic_user = loads(json_user)
        self.hostid = hostid
        self.username = dic_user['username']
        self.uid = dic_user['uid']
        self.gid = dic_user['gid']
        self.description = dic_user['description']

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_username(self,username):
        self.username = username

    def set_uid(self,uid):
        self.uid = uid

    def set_gid(self,gid):
        self.gid = gid

    def set_description(self,desc):
        self.description = desc

    def get_hostid(self):
        return self.hostid

    def get_username(self):
        return self.username

    def get_uid(self):
        return self.uid

    def get_gid(self):
        return self.gid

    def get_description(self):
        return self.description

    def get_dic(self):
        dic_user = {
            'hostid':self.hostid,
            'uid':self.uid,
            'gid':self.gid,
            'username':self.username,
            'description':self.description
        }
        return dic_user
