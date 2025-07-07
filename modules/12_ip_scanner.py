# pip install scapy
from scapy.all import *

def ip_scan(target_network):
    ans, unans = sr(IP(dst=target_network)/ICMP(), timeout=2, verbose=0)
    for snd, rcv in ans:
        print(f"IP: {rcv.src} is up")

if __name__ == "__main__":
    ip_scan('192.168.1.0/24')