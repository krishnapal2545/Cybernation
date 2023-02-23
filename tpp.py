from ipaddress import *

out =  IPv4Interface('192.168.10.5/24').netmask
print(out)