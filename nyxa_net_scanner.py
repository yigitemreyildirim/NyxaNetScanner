import scapy.all as scapy

arp_request_packet = scapy.ARP(pdst="192.168.1.1")
brodcast_packet = scapy.Ether(dst ="ff:ff:ff:ff:ff")

combined_packet = brodcast_packet/arp_request_packet

result = scapy.srp(combined_packet, timeout=1)
