from json import loads


class Host:
    def __init__(self, str_host_info, str_cpu_info, str_disk_info, str_wsc, str_uptime, str_os_info):
        # remove the [] brackets
        str_host_info = str_host_info.replace("[","")
        self.str_host_info = str_host_info.replace("]","")

        str_cpu_info = str_cpu_info.replace("[","")
        self.str_cpu_info = str_cpu_info.replace("]","")

        str_disk_info = str_disk_info.replace("[","")
        self.str_disk_info = str_disk_info.replace("]","")

        str_wsc = str_wsc.replace("[","")
        self.str_wsc = str_wsc.replace("]","")

        str_uptime = str_uptime.replace("[","")
        self.str_uptime = str_uptime.replace("]","")

        str_os_info =  str_os_info.replace("[","")
        self.str_os_info = str_os_info.replace("]","")

        # convert STR to dictionary
        host_info = loads(self.str_host_info)
        cpu_info = loads(self.str_cpu_info)
        disk_info = loads(self.str_disk_info)
        wsc = loads(self.str_wsc)
        uptime = loads(self.str_uptime)
        os_info = loads(self.str_os_info)

        # initials the object attributes
        self.uuid = host_info["uuid"]
        self.host_name = host_info["hostname"]
        self.physical_memory = str(int(host_info["physical_memory"]) / 1048576)
        self.cpu_model = cpu_info["model"]
        self.number_of_cores = cpu_info["number_of_cores"]
        self.current_clock_speed = cpu_info["current_clock_speed"]
        self.disk_index = disk_info["disk_index"]
        self.disk_size = str(int(disk_info["disk_size"]) / 1048576)
        self.disk_id = disk_info["id"]
        self.num_of_partitions = disk_info["partitions"]
        self.disk_type = disk_info["type"]
        self.antivirus = wsc["antivirus"]
        self.autoupdate = wsc["autoupdate"]
        self.firewall = wsc["firewall"]
        self.user_account_control = wsc["user_account_control"]
        self.windows_security_center_service = wsc["windows_security_center_service"]
        self.uptime_day = uptime["days"]
        self.uptime_hour = uptime["hours"]
        self.uptime_minute = uptime["minutes"]
        self.os_arch = os_info["arch"]
        self.os_build = os_info["build"]
        self.os_name = os_info["name"]
        self.os_version = os_info["version"]

    def set_host_uuid(self, host_uuid):
        self.uuid = host_uuid

    def set_host_hostname(self, host_name):
        self.host_name = host_name

    def set_host_memory(self, memory):
        self.physical_memory = memory

    def set_cpu_model(self, model):
        self.cpu_model = model

    def set_cpu_number_of_cores(self, number_of_cores):
        self.number_of_cores = number_of_cores

    def set_current_clock_speed(self, speed):
        self.current_clock_speed = speed

    def set_disk_index(self, index):
        self.disk_index = index

    def set_disk_size(self, size):
        self.disk_size = size

    def set_disk_id(self, disk_id):
        self.disk_id = disk_id

    def set_num_of_partitions(self, num):
        self.num_of_partitions = num

    def set_disk_type(self, disk_type):
        self.disk_type = disk_type

    def set_antivirus(self, antivirus):
        self.antivirus = antivirus

    def set_autoupdate(self, autoupdate):
        self.autoupdate = autoupdate

    def set_firewall(self, firewall):
        self.firewall = firewall

    def set_user_account_control(self, user_account_control):
        self.user_account_control = user_account_control

    def set_uptime_day(self, uptime_day):
        self.uptime_day = uptime_day

    def set_uptime_hour(self, uptime_hour):
        self.uptime_hour = uptime_hour

    def set_uptime_minute(self, uptime_minute):
        self.uptime_minute = uptime_minute

    def set_os_arch(self, os_arch):
        self.os_arch = os_arch

    def set_os_build(self, os_build):
        self.os_build = os_build

    def set_os_name(self, os_name):
        self.os_name = os_name

    def set_os_version(self, os_version):
        self.os_version = os_version

    def set_host_info(self, host_info):
        self.uuid = host_info["uuid"]
        self.host_name = host_info["hostname"]
        self.physical_memory = host_info["physical_memory"]

    def set_cpu_info(self, cpu_info):
        self.cpu_model = cpu_info["model"]
        self.number_of_cores = cpu_info["number_of_cores"]
        self.current_clock_speed = cpu_info["current_clock_speed"]

    def set_disk_info(self, disk_info):
        self.disk_index = disk_info["disk_index"]
        self.disk_size = (disk_info["disk_size"] * 1048576)
        self.disk_id = disk_info["id"]
        self.num_of_partitions = disk_info["partitions"]
        self.disk_type = disk_info["type"]

    def set_wsc_info(self, wsc):
        self.antivirus = wsc["antivirus"]
        self.autoupdate = wsc["autoupdate"]
        self.firewall = wsc["firewall"]
        self.user_account_control = wsc["user_account_control"]
        self.windows_security_center_service = wsc["windows_security_center_service"]

    def set_uptime(self, uptime):
        self.uptime_day = uptime["days"]
        self.uptime_hour = uptime["hours"]
        self.uptime_minute = uptime["minutes"]

    def set_os_info(self, os_info):
        self.os_arch = os_info["arch"]
        self.os_build = os_info["build"]
        self.os_name = os_info["name"]
        self.os_version = os_info["version"]

    def get_host_uuid(self):
        return self.uuid

    def get_host_hostname(self):
        return self.host_name

    def get_host_memory(self):
        return self.physical_memory

    def get_cpu_model(self):
        return self.cpu_model

    def get_cpu_number_of_cores(self):
        return self.number_of_cores

    def get_current_clock_speed(self):
        return self.current_clock_speed

    def get_disk_index(self):
        return self.disk_index

    def get_disk_size(self):
        return self.disk_size

    def get_disk_id(self):
        return self.disk_id

    def get_num_of_partitions(self):
        return self.num_of_partitions

    def get_disk_type(self):
        return self.disk_type

    def get_antivirus(self):
        return self.antivirus

    def get_autoupdate(self):
        return self.autoupdate

    def get_firewall(self):
        return self.firewall

    def get_user_account_control(self):
        return self.user_account_control

    def get_uptime_day(self):
        return self.uptime_day

    def get_uptime_hour(self):
        return self.uptime_hour

    def get_uptime_minute(self):
        return self.uptime_minute

    def get_os_arch(self):
        return self.os_arch

    def get_os_build(self):
        return self.os_build

    def get_os_name(self):
        return self.os_name

    def get_os_version(self):
        return self.os_version

    def get_host_info(self):
        host_info = {
            "uuid": self.uuid,
            "hostname": self.host_name,
            "physical_memory": self.physical_memory
        }
        return host_info

    def get_cpu_info(self):
        cpu_info = {
            "model": self.cpu_model,
            "number_of_cores": self.number_of_cores,
            "current_clock_speed": self.current_clock_speed
        }
        return cpu_info

    def get_disk_info(self):
        disk_info = {
            "disk_index": self.disk_index,
            "disk_size": self.disk_size,
            "id": self.disk_id,
            "number_of_partitions": self.num_of_partitions,
            "type": self.disk_type
        }
        return disk_info

    def get_wsc_info(self):
        wsc_info = {
            "antivirus": self.antivirus,
            "autoupdate": self.autoupdate,
            "firewall": self.firewall,
            "user_account_control": self.user_account_control,
            "windows_security_center_service": self.windows_security_center_service
        }
        return wsc_info

    def get_uptime(self):
        uptime = {
            "days": self.uptime_day,
            "hours": self.uptime_hour,
            "minutes": self.uptime_minute,
        }
        return uptime

    def get_os_info(self):
        os_info = {
            "arch": self.os_arch,
            "build": self.os_build,
            "name": self.os_name,
            "version": self.os_version
        }
        return os_info

    def get_dic(self):
        new_dic = {
            "uuid": self.uuid,
            "host_name": self.host_name,
            "memory": self.physical_memory,
            "cpu_info": self.get_cpu_info(),
            "disk_info": self.get_disk_info(),
            "os_info": self.get_os_info(),
            "windows_security_center": self.get_wsc_info(),
            "uptime": self.get_uptime()
        }
        return new_dic
