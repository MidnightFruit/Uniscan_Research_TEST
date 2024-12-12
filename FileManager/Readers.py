from Characteristics.Characteristics import MeasurerCharacteristic
from Measurments.Measurment import Measurment
from .utils import convert_ip_str_int


def read_measurer_from_file(file_name: str):
    result = [] 

    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            if line.strip():
                data = line.split('\t')
                measurer = MeasurerCharacteristic(data[0], data[1], data[2], data[3])
                result.append(measurer)

    return result


def read_data_from_file(file_name: str):
    result = []
    
    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            if line.strip():
                data = line.split('\t')
                measurment = Measurment(convert_ip_str_int(data[0]), data[1], data[2])
                result.append(measurment)
                
    return result
