from struct import unpack
import socket

class IPv4:
    def __init__(self, data):
        maindata = data
        data = unpack('!BBHHHBBH4s4s', data[:20])
        self.version = data[0] >> 4
        self.ihl = (data[0] & 0xf) * 4
        self.length = data[1]
        self.identifier = data[2]
        self.xdm = data[4] >> 13
        self.frag_offset = data[4]
        self.ttl = data[5] 
        self.protocol = data[6] 
        self.header_checksum = data[7] 
        self.src_add = socket.inet_ntoa(data[8])
        self.dest_add = socket.inet_ntoa(data[9])
        self.data = maindata[self.ihl:]


        