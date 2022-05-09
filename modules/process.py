from json import loads
class Process:
    def __init__(self,json_process,hostid):
        dic_process = loads(json_process)
        self.hostid = hostid
        self.name = dic_process['name']
        self.parent = dic_process['parent']
        if dic_process['path'] != "":
            self.path = dic_process['path']
        else:
            self.path = "None"
        self.uid = dic_process['uid']
        self.pid = dic_process['pid']

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_name(self,name):
        self.name = name

    def set_parent(self,parent):
        self.parent = parent

    def set_path(self,path):
        self.path = path

    def set_uid(self,uid):
        self.uid = uid

    def set_pid(self,pid):
        self.pid = pid

    def get_hostid(self):
        return self.hostid

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_path(self):
        return self.path

    def get_uid(self):
        return self.uid

    def get_pid(self):
        return self.pid

    def get_dic(self):
        dic_data = {
            'hostid': self.hostid,
            'name': self.name,
            'path': self.path,
            'parent':self.parent,
            'uid':self.uid,
            'pid':self.pid
        }
        return dic_data
