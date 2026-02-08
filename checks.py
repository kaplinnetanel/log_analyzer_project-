from reader import *

def extracting_ip_addresses(data):
    return [a for a in data if not a[1].startswith(("10","192.168")) ]
print(extracting_ip_addresses(log_list))