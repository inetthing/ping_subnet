# -*- coding: utf-8 -*-
# pinging subnet and write in file

import ipaddress
from pythonping import ping

subnet = ipaddress.ip_network('192.168.1.0/30')
f = open('ping.txt', 'w')

def ping_add(ip_add):
    if (ping(ip_add).rtt_avg_ms == 2000): return False
    return True

for ip in subnet:
    out = str(ip) + '     '+  str(ping_add(str(ip)))
    print (out)
    f.write(out + '\n')
f.close()
