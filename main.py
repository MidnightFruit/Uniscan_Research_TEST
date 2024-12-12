from FileManager.Readers import read_data_from_file
from FileManager.utils import convert_ip_int_str


data = read_data_from_file("data.txt")
print(data)