from json import loads
class Service:
    def __init__(self,json_service,hostid):
        dic_service = loads(json_service)
        self.hostid = hostid
        self.pid = dic_service['pid']
        self.name = dic_service['name']
        self.description = dic_service['description']
        self.display_name = dic_service['display_name']
        self.status = dic_service['status']
        self.user_account = dic_service['user_account']

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_pid(self,pid):
        self.pid = pid

    def set_name(self,name):
        self.name = name

    def set_description(self,desc):
        self.description =desc

    def set_display_name(self,display_name):
        self.display_name = display_name

    def set_status(self,status):
        self.status = status

    def set_user_account(self,user_acc):
        self.user_account = user_acc

    def get_hostid(self):
        return self.hostid

    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_display_name(self):
        return self.display_name

    def get_status(self):
        return self.status

    def get_user_account(self):
        return self.user_account

    def get_dic(self):
        dic_service = {
            'hostid':self.hostid,
            'pid':self.pid,
            'name':self.name,
            'description':self.description,
            'display_name':self.display_name,
            'status':self.status,
            'user_account':self.user_account
        }
        return dic_service