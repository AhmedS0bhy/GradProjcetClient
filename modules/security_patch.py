from json import loads

class Security_patch:
    def __init__(self,json_patch ,hostid):
        dic_patch  = loads(json_patch)
        self.hostid = hostid
        self.csname = dic_patch['csname']
        self.caption = dic_patch['caption']
        self.description = dic_patch['description']
        self.hotfix_id = dic_patch['hotfix_id']

    def set_hostid(self,hostid):
        self.hostid = hostid

    def set_csname(self,csname):
        self.csname = csname

    def set_caption(self,caption):
        self.caption = caption

    def set_descriotion(self,desc):
        self.description = desc

    def set_hotfix_id(self,hotfix):
        self.hotfix_id = hotfix

    def get_hostid(self):
        return self.hostid

    def get_csname(self):
        return self.csname

    def get_caption(self):
        return self.caption

    def get_description(self):
        return self.description

    def get_hotfix_id(self):
        return self.hotfix_id

    def get_dic(self):
        dic_patch = {
            'hostid': self.hostid,
            'csname': self.csname,
            'caption': self.caption,
            'description': self.description,
            'hotfix_id': self.hotfix_id
        }
        return dic_patch