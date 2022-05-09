
class Sysmon_event:
    def __init__(self,event_data,hostid):
        event_Data_list = event_data.split("\r\n")
        list_of_values = []
        tmp_id = event_Data_list[0].split(":")
        list_of_values.append(tmp_id[1].replace(",",""))

        message_List = event_Data_list[1].split("\\r\\n")
        for message in message_List:
            tmp = message.split(": ")
            list_of_values.append(tmp[1])
        # assing the values to the object for event ID 1
        self.hostid = hostid
        self.id = list_of_values[0].replace("  ","")
        self.rule_name = list_of_values[2]
        self.utctime = list_of_values[3]
        self.process_guid = list_of_values[4]
        self.process_id = list_of_values[5]
        self.image = list_of_values[6].replace("\\\\","/")
        self.file_version = list_of_values[7]
        self.description = list_of_values[8]
        self.product = list_of_values[9]
        self.company = list_of_values[10]
        self.original_file_name = list_of_values[11]
        self.command_line = list_of_values[12].replace("\\\\","/")
        self.current_directory = list_of_values[13].replace("\\\\","/")
        self.user = list_of_values[14].replace("\\\\","/")
        self.logon_guid = list_of_values[15]
        self.logon_id = list_of_values[16]
        self.terminal_session_id = list_of_values[17]
        self.integrity_level = list_of_values[18]
        self.hash = list_of_values[19].replace("MD5=","")
        self.parent_process_guid = list_of_values[20]
        self.parent_process_id = list_of_values[21]
        self.parent_image = list_of_values[22].replace("\\\\","/")
        self.parent_command_line = list_of_values[23].replace("\\\\","/")
        self.parent_user = list_of_values[24].replace("\\\\","/")

    def get_hostid(self):
        return self.hostid

    def set_hostid(self,hostid):
        self.hostid = hostid

    def get_id(self):
        return self.id

    def set_id(self,id):
        self.id = id

    def get_rule_name(self):
        return self.rule_name

    def set_rule_name(self,rulename):
        self.rule_name = rulename

    def get_utctime(self):
        return self.utctime

    def set_utctime(self,utctime):
        self.utctime = utctime

    def get_process_guid(self):
        return self.process_guid

    def set_process_guid(self,guid):
        self.process_guid = guid

    def get_process_id(self):
        return self.process_id

    def set_process_id(self,id):
        self.process_id = id

    def get_image(self):
        return self.image

    def set_image(self,image):
        self.image = image

    def get_file_version(self):
        return self.file_version

    def set_file_version(self,file_version):
        self.file_version = file_version

    def get_description(self):
        return self.description

    def set_description(self,desc):
        self.description =desc

    def get_product(self):
        return self.product

    def set_product(self,product):
        self.product = product

    def get_company(self):
        return self.company

    def set_company(self,company):
        self.company = company

    def get_original_file_name(self):
        return self.original_file_name

    def set_original_file_name(self,ofn):
        self.original_file_name = ofn

    def get_command_line(self):
        return self.command_line

    def set_command_line(self,cml):
        self.command_line = cml

    def get_current_directory(self):
        return self.current_directory

    def sset_current_directory(self,cd):
        self.current_directory = cd

    def get_user(self):
        return self.user

    def set_user(self,user):
        self.user = user

    def get_logon_guid(self):
        return self.logon_guid

    def set_logon_guid(self, logon_guid):
        self.logon_guid = logon_guid

    def get_logon_id(self):
        return self.logon_id

    def set_logon_id(self, logon_id):
        self.logon_id = logon_id

    def get_terminal_session_id(self):
        return self.terminal_session_id

    def set_terminal_session_id(self, session_id):
        self.terminal_session_id = session_id

    def get_integrity_level(self):
        return self.integrity_level

    def set_integrity_level(self, int_level):
        self.integrity_level = int_level

    def get_hash(self):
        return self.hash

    def set_hash(self, hash):
        self.hash = hash

    def get_parent_process_guid(self):
        return self.parent_process_guid

    def set_parent_process_guid(self, pp_guid):
        self.parent_process_guid = pp_guid

    def get_parent_process_id(self):
        return self.parent_process_id

    def set_parent_prcess_id(self, pp_id):
        self.parent_process_id = pp_id

    def get_parent_image(self):
        return self.parent_image

    def set_parent_image(self, p_image):
        self.parent_image = p_image

    def get_parent_command_line(self):
        return self.parent_command_line

    def set_parent_command_line(self, parent_command_line):
        self.parent_command_line = parent_command_line

    def get_parent_user(self):
        return self.parent_user

    def set_parent_user(self,p_user):
        self.parent_user  = p_user

    def get_dic(self):
        if self.id == "1":
            dic_data = {
                    "hostid":self.hostid,
                    "id": self.id,
                    "RuleName": self.rule_name,
                    "UtcTime": self.utctime,
                    "ProcessGuid": self.process_guid,
                    "ProcessId": self.process_id,
                    "Image": self.image,
                    "FileVersion":self.file_version,
                    "Description":self.description,
                    "Product": self.product,
                    "Company": self.company,
                    "OriginalFileName": self.original_file_name,
                    "CommandLine": self.command_line,
                    "CurrentDirectory":self.current_directory,
                    "User":self.user,
                    "LogonGuid":self.logon_guid,
                    "LogonId":self.logon_id,
                    "TerminalSessionId":self.terminal_session_id,
                    "IntegrityLevel":self.integrity_level,
                    "Hashes":self.hash,
                    "ParentProcessGuid":self.parent_process_guid,
                    "ParentProcessId":self.process_id,
                    "ParentImage":self.parent_image,
                    "ParentCommandLine":self.parent_command_line,
                    "ParentUser":self.parent_user
            }
        return dic_data