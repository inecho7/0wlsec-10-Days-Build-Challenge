import ipaddress
import socket

target_input = input("Enter the target Network (e.g. 192.168.1.0/24)")
network = ipaddress.ip_network(target_input, strict=False)
host_list = network.hosts()
print("Select the type of scan you want")
print("1. Fast Scan (Scan top 10 most common ports)")
print("2. Deep Scan (Scan a range of ports (1, 1025))")

choice = input("Enter choice (1 or 2): ")
if choice == "1":
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445]
elif choice == "2":
    ports_to_scan = list(range(1, 1025))
else:
    print("Error: Please enter a valid choice")
    ports_to_scan = []

for ip in host_list:
    for port in ports_to_scan:  
        s = socket.socket()
        s.settimeout(1.0)
        print(f"Scanning {ip} on port {port}")
        result = s.connect_ex((str(ip), port))
        if result == 0:
            print(f"Host {ip} {port} is active!")
