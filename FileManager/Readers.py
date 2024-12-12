from datetime import datetime

from Characteristics.Characteristics import MeasurerCharacteristic
from Measurments.Measurment import Measurment
from .utils import convert_ip_str_int


def read_measurer_from_file(file_name: str):
    result = [] 

    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            if line.strip():
                measurer = MeasurerCharacteristic()
                data = line.split('\t')
                measurer.IP_ADRESS = int(data[0])
                measurer.RANGE_START = float(data[1])
                measurer.RANGE_STOP = float(data[2])
                measurer.UNIT = data[3]
                result.append(measurer)

    return result


def read_data_from_file(file_name: str):
    result = []
    date_time_format = "%Y.%m.%d %H:%M:%S.%f"
    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            if line.strip():
                measurment = Measurment()
                data = line.split('\t')
                measurment.IP_ADRESS = convert_ip_str_int(data[0])
                measurment.TIMESTAMP = datetime.strptime(data[1], date_time_format)
                measurment.VALUE = float(data[2])
                result.append(measurment)
    return result
