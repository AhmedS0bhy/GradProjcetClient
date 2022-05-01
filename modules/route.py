from json import loads
class Route:
    def __init__(self,json_route,hostid):
        dic_route = loads(json_route)
        self.hostid = hostid
        self.source = dic_route['source']
        self.netmask = dic_route['netmask']
        self.interface = dic_route['interface']
        self.gateway = dic_route['gateway']
        self.destination = dic_route['destination']

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_source(self,source):
        self.source = source

    def set_netmask(self,netmask):
        self.netmask = netmask

    def set_gateway_interface(self,gateway_interface):
        self.gateway_interface = gateway_interface

    def set_destination(self,dest):
        self.destination = dest

    def get_hostid(self):
        return self.hostid

    def get_source(self):
        return self.source

    def get_netmask(self):
        return self.netmask

    def get_gateway_interface(self):
        return self.gateway_interface

    def get_destination(self):
        return self.destination

    def get_dic(self):
        dic_route = {
            'hostid':self.hostid,
            'source':self.source,
            'netmask':self.netmask,
            'gateway':self.gateway,
            "interface": self.interface,
            'destination':self.destination
        }
        return dic_route
