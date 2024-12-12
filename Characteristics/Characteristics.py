

class MeasurerCharacteristic:
    def __init__(self, ip: str, range_start, range_stop, unit):
        self.IP_ADRESS = int(ip)
        self.RANGE_START = float(range_start)
        self.RANGE_STOP = float(range_stop)
        self.UNIT = unit

    def __repr__(self):
        return f"IP: {self.IP_ADRESS}\tSTART: {self.RANGE_START}\tSTOP: {self.RANGE_STOP}\t UNITS: {self.UNIT}\n"
