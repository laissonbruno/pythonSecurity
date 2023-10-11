import ipaddress

ip = '192.168.0.1'
ip2 = '192.168.0.0/24'

endereco = ipaddress.ip_address(ip)
print(endereco)

rede = ipaddress.ip_network(ip2, strict=False)
print(rede)

for ip in rede:
    print(rede)

