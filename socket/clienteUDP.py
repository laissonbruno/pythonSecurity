import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente socket criado com sucesso!")

host = 'localhost'
porta = 5433
mensagem = 'O servidor está online?'

try:
    print(f'Cliente: {mensagem}')
    s.sendto(mensagem.encode(), (host, porta))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}')
finally:
    print('Cliente: Fechando a conexão')
    s.close()