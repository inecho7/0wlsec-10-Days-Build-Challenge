import ipaddress
import socket

target_input = input("Enter the target Network (e.g. 192.168.1.0/24)")
network = ipaddress.ip_network(target_input, strict=False)
host_list = network.hosts()
for ip in host_list:
    s = socket.socket()
    s.settimeout(1.0)
    result = s.connect_ex((str(ip), 80))
    if result == 0:
        print(f"Host {ip} is active!")
        