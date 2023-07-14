from scapy.layers.l2 import Ether, ARP

from scapy.sendrecv import srp

ip_scan = '172.18.20.0/24'
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_scan), timeout=2)
ans.summary(lambda s, r: r.sprintf("%Ether.src% %ARP.psrc%"))
