# from pprint import pprint
# from netmiko import (ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException)

# device = {
#     "device_type": "cisco_xe",
#     "host":"192.168.20.254",
#     "username" : "admin",
#     "password": "cisco",
#     "secret":"a223B",
# }

# try:
#     with ConnectHandler(**device) as ssh:
#         ssh.enable()
#         output = ssh.send_command("sh users")
#         print(output)
# except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
#     print(e)

import telnetlib
tn = telnetlib.Telnet('192.168.10.6',5001)
tn.read_very_eager()
tn.write("sh ip int br".encode('ascii') + b"\n")
tn.write("\n".encode('ascii'))
tn.read_until(b"#")
print(tn.read_all())
# with telnetlib.Telnet ('172.17.23.254') as telnet:
#                     telnet.read_until(b"Username")
#                     telnet.write('admin'.encode('ascii')+b"\n")
#                     telnet.read_until(b"Password")
#                     telnet.write('cisco'.encode('ascii')+b"\n")
#                     index, m, output = telnet .expect([b">",b"#"])
#                     if index == 0:
#                         telnet.write(b"enable \n")
#                         telnet.read_until(b"Password")
#                         telnet.write('a223B'.encode('ascii')+b"\n")
#                         telnet.read_until (b"#", timeout=5) 
#                         telnet.write(b"terminal length 0\n")
#                     telnet.read_until(b"#", timeout=5) 
#                     # time.sleep(3)