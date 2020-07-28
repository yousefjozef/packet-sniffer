import struct
import socket
import Ethernet
from ipv4 import IPv4
from tcp import TCP
from udp import UDP



sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
raw_data, add = sniffer.recvfrom(4096)
eth = Ethernet.Ethernet(raw_data)

print(eth.frame)
print (eth.src_mac)
print(eth.dest_mac)
print(eth.proto)

#ipv4
if eth.proto == 2048:
    packet = IPv4(eth.data)
    print(packet.dest_add)
    print(packet.src_add)
    print(packet.protocol)
    if packet.protocol == 6:
        tcp = TCP(packet.data)
        print(tcp.src_port)
        print(tcp.dest_port)
    
    elif packet.protocol == 17:
        udp = UDP(packet.data)
        print(udp.src_port)
        print(udp.dest_port)
    








#arp
elif eth.proto == 2054:
    print('arp')
    #idk





