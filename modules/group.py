from json import loads

class Group:
    def __init__(self,json_group,hostid):
        dic_group = loads(json_group)
        self.hostid = hostid
        self.gid = dic_group['gid']
        self.groupname = dic_group['groupname']
        self.comment = dic_group['comment']

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_gid(self,gid):
        self.gid = gid

    def set_groupname(self,groupname):
        self.groupname = groupname

    def set_comment(self,comment):
        self.comment = comment

    def get_gid(self):
        return self.gid

    def get_hostid(self):
        return  self.hostid

    def get_groupname(self):
        return self.groupname

    def get_comment(self):
        return self.comment

    def get_dic(self):
        dic_group = {
            'hsotid': self.hostid,
            'gid':self.gid,
            'groupname':self.groupname,
            'comment':self.comment
        }
        return dic_group