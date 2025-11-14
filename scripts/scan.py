# Code used to conduct ping sweep and syn scans on all ports from 172.125.125.0/24

#!/usr/bin/python3
from scapy.all import *

subnet = "172.16.125."
start_ip = 1
end_ip = 254
port = 22

def ping_sweep():
  active_user = []
  for i in range(start_ip, end_ip+1):
    ip = subnet + str(i)
    pkt = IP(dst=ip)/ICMP()
    reply = sr1(pkt, timeout=0.5, verbose=0)
    if reply:
      print(f"Host {ip} is up")
      active_user.append(ip)
  return active_user

def tcp_syn_scan(users):
  for ip in users:
    ip = IP(dst=ip)
    tcp = TCP(dport=port, flags="S")
    syn = ip/tcp
    response = sr1(syn, timeout=0.5, verbose=0)
    
    if response:
      if response.haslayer(TCP) and respone.getlayer(TCP).flags == 0x12:
        print(f"Port {port} is open on {ip}")
      elif reponse.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        print(f"Port {port} is closed on {ip}")
      else:
        print(f"No reponse from {ip}")

active = ping_sweep()
tcp_syn_scan(active)
