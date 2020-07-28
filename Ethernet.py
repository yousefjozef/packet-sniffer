import struct
from socket import htons


class Ethernet:
    def __init__(self, raw_data):
        self.frame = raw_data
        frame = struct.unpack('! 6s 6s  H', raw_data[:14])
        self.src_mac = self.__mac_add(frame[1])
        self.dest_mac = self.__mac_add(frame[0])
        self.proto = frame[2]
        self.data = raw_data[14:]
    
    def __mac_add(self, raw):
        braw = map('{:02x}'.format, raw)
        mac = ':'.join(braw).upper()
        return mac


#eth = Ethernet(b'ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')
#print('end')