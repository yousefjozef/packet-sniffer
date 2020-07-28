import string

class HTTP:
    def __init__(self, raw_data):
        try:
            data = raw_data.decode('utf-8')
            
        except:
            data = raw_data
        
        self.data = ''.join(data).replace('\n\r', '\n')
