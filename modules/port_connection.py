from json import loads

class Port_connection:
    def __init__(self,json_conn,hostid):
        dic_conn  = loads(json_conn)
        self.hostid = hostid
        self.pid = dic_conn['pid']
        self.address = dic_conn['address']
        self.path = dic_conn['path']
        self.port = dic_conn['port']

    def set_hostid(self,hostid):
        self.hostid

    def set_pid(self,pid):
        self.pid

    def set_address(self,address):
        self.address

    def set_path(self,path):
        self.path

    def set_port(self,port):
        self.port = port

    def get_hostid(self):
        return self.hostid

    def get_pid(self):
        return self.pid

    def get_address(self):
        return self.address

    def get_port(self):
        return self.port

    def get_dic(self):
        dic_json = {
            'hostid':self.hostid,
            'pid':self.pid,
            'address':self.address,
            'port':self.port
        }
        return dic_json
