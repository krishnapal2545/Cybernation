import telnetlib
from netmiko import (ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException)
import time
from manage import *
from datetime import datetime
from pprint import pprint
from tkinter import ttk, messagebox


def to_bytes(line): return f"{line}\n".encode("utf-8")


def typeconfig(config):
    name = config['Name']
    if name == 'Static Routing':
        staticRouting = ["configure terminal",
                         f"ip route {config['Network-IP']} {config['Network-SubIP']} {config['NextHop']}", "end"]
        return staticRouting
    elif name == 'RIP Routing':
        ripRouting = ["configure terminal", "router rip", f"version {config['Version']}",
                      f"network {config['Network-IP']}", "no auto-summary", "end"]
        return ripRouting
    elif name == 'EIGRP Routing':
        eigrpRouting = ["configure terminal",
                        f"router eigrp {config['ASnumber']}", f"network {config['Network-IP']}", "end"]
        return eigrpRouting
    elif name == 'OSPF Routing':
        ospfRouting = ["configure terminal",f"router ospf {config['Process-ID']}", 
                       f"network {config['Network-IP']} {config['Network-SubIP']} area {config['Area']}", "end"]
        return ospfRouting
    else:
        return []


def routing(config, window):
    try:
        with telnetlib.Telnet(config['IP']) as telnet:
            telnet.read_until(b"Username")
            telnet.write(to_bytes(config['Username']))
            telnet.read_until(b"Password")
            telnet.write(to_bytes(config['Password']))
            index, m, output = telnet.expect([b">", b"#"])
            if index == 0:
                telnet.write(b"enable\n")
                telnet.read_until(b"Password")
                telnet.write(to_bytes(config['Enable']))
                telnet.read_until(b"#", timeout=5)
            telnet.write(b"terminal length 0\n")
            telnet.read_until(b"#", timeout=5)
            time.sleep(3)
            telnet.read_very_eager()

            result = {}
            commands = typeconfig(config)
            for command in commands:
                telnet.write(to_bytes(command))
                output = telnet.read_until(b"#", timeout=5).decode("utf-8")
                result[command] = output.replace("\r\n", "\n")
            telnet.write(to_bytes("show running-config"))
            output = telnet.read_until(b"#", timeout=5).decode("utf-8")
            result["show running-config"] = output.replace("\r\n", "\n")
            pprint(result, width=120)
            saveconfig(config)
            return result
    except TimeoutError as e:
        messagebox.showerror("Error", e, parent=window)

def netmikoRouting(config, window):
    device = {
        'device_type': config['Device_Type'],
        'host': config['IP'],
        'username': config['Username'],
        'password': config['Password'],
        'secret': config['Enable'],
    }
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            commands = typeconfig(config)
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        pprint(result, width=120)
        saveconfig(config)
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
        messagebox.showerror("Error", error, parent=window)


if __name__ == "__main__":
    config = {
        'deviceID': 3,
        'Name': 'Static Routing',
        'Device_Type': 'cisco_ios',
        'Username': 'admin',
        'Password': 'cisco',
        'Enable': 'a223B',
        'IP': '192.168.10.2',
        'Network-IP': '192.168.20.0',
        'Network-SubIP': '255.255.25.0',
        'NextHop': '10.10.10.1',
        'Last_Modify': datetime.today()
    }

    routing(config)
