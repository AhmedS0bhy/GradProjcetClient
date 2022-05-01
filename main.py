from modules.process import Process
from modules.service import Service
from modules.arp import Arp
from modules.event import Event
from modules.group import Group
from modules.host import Host
from modules.interface import Interface
from modules.port_connection import Port_connection
from modules.route import Route
from modules.security_patch import Security_patch
from modules.session import Session
from modules.software import Software
from modules.sysmon_event import Sysmon_event
from modules.user import User
from modules.user_group import User_group
from json import dumps, loads
from subprocess import run, PIPE
from datetime import datetime
from requests import post


def get_proceesses():
    processes = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT pid,name,path,uid,parent FROM processes'}"],
        stdout=PIPE)
    str_Data = processes.stdout.decode('ascii')
    return str_Data

def get_cpu_info():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT model,number_of_cores,Current_clock_speed FROM cpu_info'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_os_info():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT name,version,patch,build,arch FROM os_version'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_disk_info():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT partitions,disk_index,type,id,disk_size,name FROM disk_info'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_installed_programs():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT name,version,install_location,publisher FROM programs'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_services():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT name,display_name,status,pid,description,user_account FROM services'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_sec_events():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT channel,datetime,level,eventid,data,pid FROM windows_eventlog WHERE channel=' }"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

#def get_app_events():
#    data = run([
#        "&{&osqueryi.exe --json 'SELECT channel,datetime,level,eventid,data,pid FROM windows_eventlog WHERE channel=' }"],
#        stdout=PIPE)
#    str_data = data.stdout.decode('ascii')
#    return str_data



def get_net_connects():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT pid,port,address,path FROM listening_ports'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_groups():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT gid,groupname,comment FROM groups'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_net_route():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT destination,netmask,gateway,source,interface FROM routes'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_win_sec_center():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{& osqueryi.exe --json 'SELECT firewall,autoupdate,antivirus,windows_security_center_service,user_account_control FROM windows_security_center'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_host_info():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT uuid,hostname,cpu_brand,physical_memory FROM System_info'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_ARP():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT address,mac,interface FROM arp_cache'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_users():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT uid,gid,username,description FROM users'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_login_users():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT type,user,host,time,pid,registry_hive FROM logged_in_users'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_patches():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT csname,hotfix_id,caption,description FROM patches'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_uptime():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT days,hours,minutes FROM uptime'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_interfaces():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT interface,address,mask FROM interface_addresses'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_users_groups():
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        "&{&osqueryi.exe --json 'SELECT uid,gid FROM user_groups'}"],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def get_sysmon_events(id,aftertime):
    command = '&{Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 30  |where {$_.timecreated -gt "'+aftertime+'" -and $_.id -eq "'+id+'"}  | select id,message | ConvertTo-Json}'
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        command
        ],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data

def handle_sysmon(sysmon,hostid):
        #------ handling the sysmon data ----------#

        # cleanning the data
        sysmon = sysmon[1:-1]
        sysmon = sysmon.replace("\\","/")
        sysmon = sysmon.replace("\"","")
        sysmon_events_list = sysmon.split("},")
        events_list = []
        for i in range(len(sysmon_events_list)):
            event = sysmon_events_list[i]
            if i != (len(sysmon_events_list)-1):
                events_list.append(event[1:])
            else:
                events_list.append(event[1:-1])

        # create a list of events objects
        event_obj_list = []
        for i in events_list:
            event_obj = Sysmon_event(i,hostid)
            event_obj_list.append(event_obj)

        return event_obj_list

def handle_data(str_data,data_type,hostid):
    #-------------! handling the data to get the API format !-----------------#

    #hadle the multi layer of string data to get one element
    str_data = str_data[1:-1]
    data_list = str_data.split("},")
    for i in range(len(data_list)):
        data_list[i] = data_list[i] + "}"
    data_list[-1] = data_list[-1].replace("]","")

    # Create a list of object for each element

    # check the object Type
    data_obj_list = []
    if data_type == "service":
        for s in data_list:
            service_obj = Service(s,hostid)
            data_obj_list.append(service_obj)
    elif data_type == "proccess":
        for p in data_list:
            process_obj = Process(p,hostid)
            data_obj_list.append(process_obj)
    elif data_type == "arp":
        for a in data_list:
            arp_obj = Arp(a,hostid)
            data_obj_list.append(arp_obj)
    elif data_type == "event":
        for e in data_list:
            event_obj = Event(e,hostid)
            data_obj_list.append(event_obj)
    elif data_type == "group":
        for g in data_list:
            group_obj = Group(g,hostid)
            data_obj_list.append(group_obj)
    elif data_type == "interface":
        for i in data_list:
            interface_obj = Interface(i,hostid)
            data_obj_list.append(interface_obj)
    elif data_type == "port_connection":
        for p in data_list:
            conn_obj = Port_connection(p,hostid)
            data_obj_list.append(conn_obj)
    elif data_type == "route":
        for r in data_list:
            route_obj = Route(r,hostid)
            data_obj_list.append(route_obj)
    elif data_type == "security_patch":
        for s in data_list:
            security_patch_obj = Security_patch(s,hostid)
            data_obj_list.append(security_patch_obj)
    elif data_type == "session":
        for s in data_list:
            session_obj = Session(s,hostid)
            data_obj_list.append((session_obj))
    elif data_type == "software":
        for s in data_list:
            software_obj = Software(s,hostid)
            data_obj_list.append(software_obj)
    elif data_type == "user":
        for u in data_list:
            user_obj = User(u,hostid)
            data_obj_list.append(user_obj)
    elif data_type == "user_group":
        for u in data_list:
            user_group_obj = User_group(u,hostid)
            data_obj_list.append(user_group_obj)
    return data_obj_list

def main():
    ip = "http://localhost:5000"
    hostslist = []
    #----------------- Host Data ----------------------------------#

    host_obj = Host(get_host_info(),get_cpu_info(),get_disk_info(),get_win_sec_center(),get_uptime(),get_os_info())
    # send data to API
    r = post(ip + "/api/v1/hosts/",json=host_obj.get_dic())
    print(f"[{datetime.now()}] Host data response code: {r.status_code}")
    if r.status_code == 201:
        hostid = r.text['data']['data']['_id']
        print(f"[{datetime.now()}] Host created successfully with ID:{hostid}")
    else:
        print(f"[{datetime.now()}] ERROR!, Response data:")
        print(dumps(loads(r.text),indent=4))



if __name__ == "__main__":
    main()


