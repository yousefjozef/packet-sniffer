from struct import unpack
import socket

class TCP():
    def __init__(self, raw_data):
        data  = unpack('!HHIIHHHH', raw_data[:20])
        self.src_port = data[0]
        self.dest_port = data[1]
        self.seq_no = data[2]
        self.ack_no = data[3]
        flags = data[4]
        self.checksum = data[5]
        self.urg_point = data[6]
        self.offset = (flags >> 12) * 4
        self.fin = flags & 1
        self.syn = flags & 2
        self.rst = flags & 4
        self.psh = flags & 8
        self.ack = flags & 16 
        self.urg = flags & 32
        self.ece = flags & 64
        self.cwr = flags & 128
        self.ns  = flags & 256
        self.data = raw_data[self.offset:]

        