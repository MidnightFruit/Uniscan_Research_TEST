class Measurment:
    def __init__(self):
        self.IP_ADRESS = None
        self.TIMESTAMP = None
        self.VALUE = None

    def __repr__(self):
        return f"IP_ADDR: {self.IP_ADRESS}\tTIMESTAMP: {self.TIMESTAMP}\tVALUE: {self.VALUE}\n"