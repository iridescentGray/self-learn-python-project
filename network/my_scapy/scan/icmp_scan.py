from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import sr

ip_scan = "172.18.20.0/28"


def scan_by_icmp():
    ans, unans = sr(iface="en0", x=IP(dst=ip_scan) / ICMP(), timeout=1)
    return ans


if __name__ == "__main__":
    ans = scan_by_icmp()
    ans.summary(lambda s, r: r.sprintf("%IP.src% is alive"))
