from datetime import datetime


class Measurment:
    def __init__(self, ip:int, time_stamp: str, value: str):
        self._date_time_format = "%Y.%m.%d %H:%M:%S.%f"
        self.IP_ADRESS = ip
        self.TIMESTAMP = datetime.strptime(time_stamp, self._date_time_format)
        self.VALUE = float(value)


    def __repr__(self):
        return f"IP_ADDR: {self.IP_ADRESS}\tTIMESTAMP: {self.TIMESTAMP}\tVALUE: {self.VALUE}\n"