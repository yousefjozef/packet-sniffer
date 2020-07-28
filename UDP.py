from struct import unpack

class UDP:
    def __init__(self, raw_data):
        header = unpack('! H H 2x H', raw_data)
        self.src_port = header[0]
        self.dest_port = header[1]
        self.length = header[2]
        self.checksum = header[3]
        self.data = raw_data[8:]
        