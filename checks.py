from reader import *

# def extracting_ip_addresses(data):
#     return [a for a in data if not a[1].startswith(("10","192.168")) ]
# print(extracting_ip_addresses(log_list))

# def filter_by_sensitive_port(data):
#     return [a for a in data if   a[3] != 23 or 3389 or 22]
#
# def filter_by_size(data):
#     return [a for a in data if int(a[-1]) > 5000]
# print(filter_by_size(log_list))

def tag_traffic_by_port(data):
    return [ "NORMAL" if int(a[-1]) > 500 else "LARGE" for a in data ]
print(tag_traffic_by_port(log_list))