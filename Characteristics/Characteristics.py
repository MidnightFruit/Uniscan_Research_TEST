

class MeasurerCharacteristic:
    def __init__(self):
        self.IP_ADRESS = None
        self.RANGE_START = None
        self.RANGE_STOP = None
        self.UNIT = None

    def __repr__(self):
        return f"IP: {self.IP_ADRESS}\tSTART: {self.RANGE_START}\tSTOP: {self.RANGE_STOP}\t UNITS: {self.UNIT}\n"
