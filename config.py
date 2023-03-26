import telnetlib
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
                         f"ip route {config['Dest-IP']} {config['Dest-SubIP']} {config['NextHop']}", "end"]
        return staticRouting
    elif name == 'RIP Routing':
        ripRouting = ["configure terminal", "router rip", f"version {config['Version']}",
                      f"network {config['Network-IP']}", "no auto-summary", "end"]
        return ripRouting
    elif name == 'EIGRP Routing':
        eigrpRouting = ["configure terminal",
                        f"router eigrp {config['ASnumber']}", f"network {config['Network-IP']}", "end"]
        return eigrpRouting
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


if __name__ == "__main__":
    config = {
        'deviceID': 3,
        'Name': 'Static Routing',
        'Username': 'admin',
        'Password': 'cisco',
        'Enable': 'a223B',
        'IP': '192.168.10.2',
        'Dest-IP': '192.168.20.0',
        'Dest-SubIP': '255.255.25.0',
        'NextHop': '10.10.10.1',
        'Last_Modify': datetime.today()
    }

    routing(config)
