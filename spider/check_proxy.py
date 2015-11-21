'''
Created on Nov 18, 2015

@author: dean
'''

import os
import socket
import fcntl
import struct

CDL_IP_PRE='10.187'
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s',  bytes(ifname[:15], 'utf-8'))
    )[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_ip_address(ifname)
                break
            except IOError:
                pass
    return ip
def has_proxy():
    ip = get_lan_ip()
    return -1 != str(ip).find(CDL_IP_PRE)
