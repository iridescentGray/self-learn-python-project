from scapy.layers.inet import IP
from scapy.sendrecv import sr

ip_scan = "172.18.20.0/24"


def scan_by_ip():
    ans, unans = sr(x=IP(dst="172.18.20.1", proto=(0, 125)) / "SCAPY", retry=2)
    return ans
