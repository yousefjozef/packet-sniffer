import struct
import socket
import Ethernet
from IPv4 import IPv4
from TCP import TCP
from UDP import UDP
from HTTP import HTTP



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
    
    #TCP
    if packet.protocol == 6:
        tcp = TCP(packet.data)
        print(tcp.src_port)
        print(tcp.dest_port)
        print(tcp.ack)
        print(tcp.seq_no, ' ', tcp.ack_no)
        print(tcp.ack)
        print(tcp.offset)
        print(tcp.src_port, " ", tcp.dest_port)

        if tcp.src_port == 80 or tcp.dest_port == 80:
            http = HTTP(tcp.data) 
            print(http.data)
          

    #UDP
    elif packet.protocol == 17:
        u = UDP(packet.data)
        print(u.src_port)
        print(u.dest_port)
        

#arp
elif eth.proto == 2054:
    print('arp')
    #idk





