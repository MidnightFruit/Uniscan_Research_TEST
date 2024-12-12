def convert_ip_str_int(IP:  str):
    parts = IP.split('.')
    for i in range(len(parts)):
        parts[i] = int(parts[i])
    ip_int = (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]
    return ip_int 


def convert_ip_int_str(IP: int):
    part_1 = (IP >> 24) & 0xFF
    part_2 = (IP >> 16) & 0xFF
    part_3 = (IP >> 8) & 0xFF
    part_4 = IP  & 0xFF

    return f"{part_1}.{part_2}.{part_3}.{part_4}"    
