from json import loads

class Software:
    def __init__(self,json_software,hostid):
        dic_software = loads(json_software)
        self.hostid = hostid
        #install_location, name, publisher, version,
        self.name = dic_software['name']
        self.publisher = dic_software['publisher']
        self.version = dic_software['version']
        self.install_location = dic_software['install_location']

    def set_hostid(self,hostid):
        self.hostid =hostid

    def set_name(self,name):
        self.name = name

    def set_publisher(self,publisher):
        self.publisher = publisher

    def set_version(self,version):
        self.version = version

    def set_install_location(self,location):
        self.install_location = location

    def get_hostid(self):
        return self.hostid

    def get_name(self):
        return self.name

    def get_publisher(self):
        return self.publisher

    def get_version(self):
        return self.version

    def get_installed_location(self):
        return self.install_location

    def get_dic(self):
        dic_software = {
            'hostid':self.hostid,
            'name':self.name,
            'publisher': self.publisher,
            'version':self.version,
            'installed_location':self.install_location
        }

        return dic_software