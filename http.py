

class HTTP:
    def __init__(self, raw_data):
        try:
            raw_data = raw_data.decode('utf-8')
            #header = raw_data.find('/n/r/n/r')
            