from json import loads
class Interface:
    def __init__(self,json_interface,hostid):
        dic_interface = loads(json_interface)
        self.hostid = hostid
        self.address = dic_interface['address']
        self.interface = dic_interface['interface']
        self.mask = dic_interface['mask']

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_address(self,address):
        self.address = address

    def set_interface(self,interface):
        self.interface = interface

    def set_mask(self,mask):
        self.mask = mask

    def get_hostid(self):
        return self.hostid

    def get_address(self):
        return self.address

    def get_interface(self):
        return self.interface

    def get_mask(self):
        return self.mask

    def get_dic(self):
        dic_interface = {
            'hostid':self.hostid,
            'address': self.address,
            'interface':self.interface,
            'mask':self.mask
        }
        return dic_interface
