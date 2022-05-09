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
from datetime import datetime, timedelta
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
    return processes.stdout.decode()


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
    return data.stdout.decode()


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
    return data.stdout.decode()


def get_events(event_source, aftertime):
    command = '&{&Get-WinEvent -LogName "' + str(event_source) + '" -MaxEvents 30  |where timecreated -gt "' + str(
        aftertime) + '"  | select Id,logName,message,TimeCreated,level,processId,machineName | ConvertTo-Json}'
    data = run([
        "Powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoLogo",
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        command],
        stdout=PIPE)
    str_data = data.stdout.decode('ascii')
    return str_data


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
        "&{& osqueryi.exe --json 'SELECT firewall,autoupdate,antivirus,windows_security_center_service,\
        user_account_control FROM windows_security_center'}"],
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


def get_sysmon_events(id, aftertime):
    command = '&{&Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 30  |where {$_.timecreated -gt "' + str(
        aftertime) + '" -and $_.id -eq "' + str(id) + '"}  | select id,message | ConvertTo-Json}'
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


def handle_sysmon(sysmon_data, hostid):
    # ------ handling the sysmon data ----------#
    if "[" in sysmon_data:
        sysmon_data = sysmon_data.replace("{\r\n", "")
        sysmon_data = sysmon_data.replace('"', "")
        sysmon_data = sysmon_data.replace("[", "")
        sysmon_data = sysmon_data.replace("]", "")
        list_of_events = sysmon_data.split("},\r\n")
        list_of_events[0] = list_of_events[0][2:]
        event_obj_list = []
        for event in list_of_events:
            sysmon_obj = Sysmon_event(event, hostid)
            event_obj_list.append(sysmon_obj)
        return event_obj_list


def handle_events(str_data, hostid):
    data_obj_list = []
    if "]" in str_data:
        str_data = str_data[1:-1]
        data_list = str_data.split("},")
        for i in range(len(data_list)):
            data_list[i] = data_list[i] + "}"

        data_list[-1] = data_list[-1].replace("]", "")
        data_list[-1] = data_list[-1][:-1]

        for event in data_list:
            event_obj = Event(event, hostid)
            data_obj_list.append(event_obj)
    else:
        event_obj = Event(str_data, hostid)
        data_obj_list.append(event_obj)

    return data_obj_list


def handle_data(str_data, data_type, hostid):
    # -------------! handling the data to get the API format !-----------------#

    # hadle the multi layer of string data to get one element
    str_data = str_data[1:-1]
    data_list = str_data.split("},")
    for i in range(len(data_list)):
        data_list[i] = data_list[i] + "}"
    data_list[-1] = data_list[-1].replace("]", "")
    data_list[-1] = data_list[-1][:-1]
    # Create a list of object for each element

    # check the object Type
    data_obj_list = []
    if data_type == "service":
        for s in data_list:
            service_obj = Service(s, hostid)
            data_obj_list.append(service_obj)
    elif data_type == "proccess":
        for p in data_list:
            process_obj = Process(p, hostid)
            data_obj_list.append(process_obj)
    elif data_type == "arp":
        for a in data_list:
            arp_obj = Arp(a, hostid)
            data_obj_list.append(arp_obj)
    elif data_type == "group":
        for g in data_list:
            group_obj = Group(g, hostid)
            data_obj_list.append(group_obj)
    elif data_type == "interface":
        for i in data_list:
            interface_obj = Interface(i, hostid)
            data_obj_list.append(interface_obj)
    elif data_type == "port_connection":
        for p in data_list:
            conn_obj = Port_connection(p, hostid)
            data_obj_list.append(conn_obj)
    elif data_type == "route":
        for r in data_list:
            route_obj = Route(r, hostid)
            data_obj_list.append(route_obj)
    elif data_type == "security_patch":
        for s in data_list:
            security_patch_obj = Security_patch(s, hostid)
            data_obj_list.append(security_patch_obj)
    elif data_type == "session":
        for s in data_list:
            session_obj = Session(s, hostid)
            data_obj_list.append(session_obj)
    elif data_type == "software":
        for s in data_list:
            software_obj = Software(s, hostid)
            data_obj_list.append(software_obj)
    elif data_type == "user":
        for u in data_list:
            user_obj = User(u, hostid)
            data_obj_list.append(user_obj)
    elif data_type == "user_group":
        for u in data_list:
            user_group_obj = User_group(u, hostid)
            data_obj_list.append(user_group_obj)
    return data_obj_list


def main():
    time = datetime.now()
    bf_time = time + timedelta(minutes=-30)
    bf_time = bf_time.strftime('%Y/%m/%d %H:%M')

    hostid = ""

    ip = 'http://localhost:5000'

    hostslist = []
    # ----------------- Host Data ----------------------------------#

    host_obj = Host(get_host_info(), get_cpu_info(), get_disk_info(), get_win_sec_center(), get_uptime(), get_os_info())
    # send data to API
    r = post(ip + "/api/v1/hosts/", json=host_obj.get_dic())
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Host data response code: {r.status_code}")
    if r.status_code == 201:
        response = loads(r.text)
        hostid = response['data']['data']['_id']
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Host created successfully with ID:{hostid}")
    else:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # --------------proccesses-------------#

    proc_obj_list = handle_data(get_proceesses(), "proccess", hostid)
    proc_data_list = []
    for i in proc_obj_list:
        proc_data_list.append(i.get_dic())

    proc_data = {
        "hosts": hostslist,
        "data": proc_data_list
    }
    r = post(ip + "/api/v1/processes/", json=proc_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Processes data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # ------------Services -----------------#

    serv_obj_list = handle_data(get_services(), "services", hostid)
    serv_data_list = []
    for i in serv_obj_list:
        serv_data_list.append(i.get_dic())

    serv_data = {
        "hosts": hostslist,
        "data": serv_data_list
    }
    r = post(ip + "/api/v1/services/", json=serv_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] services data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # ---------- arp cache -----------------#

    arp_obj_list = handle_data(get_ARP(), "arp", hostid)
    arp_data_list = []
    for i in arp_obj_list:
        arp_data_list.append(i.get_dic())

    arp_data = {
        "hosts": hostslist,
        "data": arp_data_list
    }
    r = post(ip + "/api/v1/arp/", json=arp_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ARP data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # --------------- groups ------------------#

    groups_obj_list = handle_data(get_groups(), "group", hostid)
    groups_data_list = []
    for i in groups_obj_list:
        groups_data_list.append(i.get_dic())

    groups_data = {
        "hosts": hostslist,
        "data": groups_data_list
    }
    r = post(ip + "/api/v1/groups/", json=groups_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] groups data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # ---------- interfaces ---------------#

    interface_obj_list = handle_data(get_interfaces(), "interface", hostid)
    interface_data_list = []
    for i in interface_obj_list:
        interface_data_list.append(i.get_dic())

    interface_data = {
        "hosts": hostslist,
        "data": interface_data_list
    }
    r = post(ip + "/api/v1/interfaceAddresses/", json=interface_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] interface data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # ---------- net connection ----------#

    # port_connection_obj_list = handle_data(get_net_connects(), "port_connection", hostid)
    # port_connection_data_list = []
    # for i in port_connection_obj_list:
    #     port_connection_data_list.append(i.get_dic())
    #
    # port_connection_data = {
    #     "hosts": hostslist,
    #     "data": port_connection_data_list
    #     }
    # r = post(ip + "/api/v1/listenPorts/", json=port_connection_data)
    # print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] network connection data response code: {r.status_code}")
    # if r.status_code != 200:
    #     print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
    #     print(dumps(loads(r.text), indent=4))

    # --------- route table -----------#

    route_obj_list = handle_data(get_net_route(), "route", hostid)
    route_data_list = []
    for i in route_obj_list:
        route_data_list.append(i.get_dic())

    route_data = {
        "hosts": hostslist,
        "data": route_data_list
    }
    r = post(ip + "/api/v1/route/", json=route_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] local route data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # ----------- Security Patches -------#

    sec_patch_obj_list = handle_data(get_patches(), "security_patch", hostid)
    sec_patch_data_list = []
    for i in sec_patch_obj_list:
        sec_patch_data_list.append(i.get_dic())

    sec_patch_data = {
        "hosts": hostslist,
        "data": sec_patch_data_list
    }
    r = post(ip + "/api/v1/securityPatches/", json=sec_patch_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] secuirty Patchs data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # ------------- sessions-------------#

    session_obj_list = handle_data(get_login_users(), "session", hostid)
    session_data_list = []
    for i in session_obj_list:
        session_data_list.append(i.get_dic())

    session_data = {
        "hosts": hostslist,
        "data": session_data_list
    }
    r = post(ip + "/api/v1/sessions/", json=session_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] sessions data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # ----------installed software------------#

    software_obj_list = handle_data(get_installed_programs(), "software", hostid)
    software_data_list = []
    for i in software_obj_list:
        software_data_list.append(i.get_dic())

    software_data = {
        "hosts": hostslist,
        "data": software_data_list
    }
    r = post(ip + "/api/v1/installedSoftware/", json=software_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Installed software data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # ----------users------------#

    users_obj_list = handle_data(get_users(), "user", hostid)
    users_data_list = []
    for i in users_obj_list:
        users_data_list.append(i.get_dic())

    users_data = {
        "hosts": hostslist,
        "data": users_data_list
    }
    r = post(ip + "/api/v1/localUsers/", json=users_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Local users data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    # -------groups members--------#

    groups_members_obj_list = handle_data(get_users_groups(), "user_group", hostid)
    groups_members_data_list = []
    for i in groups_members_obj_list:
        groups_members_data_list.append(i.get_dic())

    groups_members_data = {
        "hosts": hostslist,
        "data": groups_members_data_list
    }
    r = post(ip + "/api/v1/usersGroups/", json=groups_members_data)
    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Local groups members data response code: {r.status_code}")
    if r.status_code != 200:
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
        print(dumps(loads(r.text), indent=4))

    while True:

        # -------- Application Events---------#

        application_events_data = get_events("Application", bf_time)
        if len(application_events_data) <= 9:
            print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] No New Application log data to send")
        else:
            app_event_obj_list = handle_events(application_events_data, hostid)
            app_event_data_list = []
            for i in app_event_obj_list:
                app_event_data_list.append(i.get_dic())
            app_events_data = {
                "hosts": hostslist,
                "data": app_event_data_list
            }

            r = post(ip + "/api/v1/application/", json=app_events_data)
            print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Application  data response code: {r.status_code}")
            if r.status_code != 200:
                print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
                print(dumps(loads(r.text), indent=4))

        # -------- System Events---------#

        system_events_data = get_events("System", bf_time)
        if len(system_events_data) <= 9:
            print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] No New Application log data to send")
        else:
            sys_event_obj_list = handle_events(system_events_data, hostid)
            sys_event_data_list = []
            for i in sys_event_obj_list:
                sys_event_data_list.append(i.get_dic())

            sys_events_data = {
                "hosts": hostslist,
                "data": sys_event_data_list
            }

            r = post(ip + "/api/v1/system/", json=sys_events_data)
            print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] System  data response code: {r.status_code}")
            if r.status_code != 200:
                print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
                print(dumps(loads(r.text), indent=4))

        # -------- Security Events---------#

        security_events_data = get_events("Security", bf_time)
        if len(security_events_data) <= 9:
            print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] No New Security log data to send")
        else:
            sec_event_obj_list = handle_events(security_events_data, hostid)
            sec_event_data_list = []
            for i in sec_event_obj_list:
                sec_event_data_list.append(i.get_dic())
            security_events_data = {
                "hosts": hostslist,
                "data": sec_event_data_list
            }

            r = post(ip + "/api/v1/security/", json=security_events_data)
            print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Security  data response code: {r.status_code}")
            if r.status_code != 200:
                print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
                print(dumps(loads(r.text), indent=4))

        # ---------- sysmon events--------#

        sysmon_obj_list = handle_sysmon(get_sysmon_events(1, bf_time), hostid)
        sysmon_data_list = []
        for i in sysmon_obj_list:
            sysmon_data_list.append(i.get_dic())

        sysmon_data = {
            "hosts": hostslist,
            "data": sysmon_data_list
        }
        print(dumps(sysmon_data, indent=4))

        r = post(ip + "/api/v1/sysmon/", json=sysmon_data)
        print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] sysmon logs response code: {r.status_code}")
        if r.status_code != 200:
            print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ERROR!, Response data:")
            print(dumps(loads(r.text), indent=4))
        break


if __name__ == "__main__":
    main()
