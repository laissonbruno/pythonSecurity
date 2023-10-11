import os

print("#" * 60)
ip_or_host = input("Digite o up ou host a ser verificado: ")
print("-" * 60)
os.system(f'ping -n 6 {ip_or_host}')
print("-" * 60)

