from json import loads

class Arp:
    def __init__(self,json_arp,hostid):
        dic_arp = loads(json_arp)
        self.hostid = hostid
        self.address = dic_arp['address']
        self.interface = dic_arp['interface']
        self.mac = dic_arp['mac']

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_address(self,address):
        self.address = address

    def set_interface(self,interface):
        self.interface = interface

    def set_mac(self,mac):
        self.mac = mac

    def get_hostid(self):
        return self.hostid

    def get_address(self):
        return self.address

    def get_interface(self):
        return self.interface

    def get_mac(self):
        return self.mac

    def get_dic(self):
        dic_arp = {
            'hostid':self.hostid,
            'address':self.address,
            'interface':self.interface,
            'mac':self.mac
        }
        return dic_arp
