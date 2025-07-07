# pip install scapy
from scapy.all import *

def port_scan(target, ports):
    for port in ports:
        pkt = IP(dst=target)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=1, verbose=0)
        if resp is not None:
            if resp.haslayer(TCP) and resp.getlayer(TCP).flags == 0x12:
                print(f"Port {port} is open")
            elif resp.haslayer(TCP) and resp.getlayer(TCP).flags == 0x14:
                print(f"Port {port} is closed")
        else:
            print(f"Port {port} is filtered")

if __name__ == "__main__":
    port_scan('target_ip', [22, 80, 443, 8080])