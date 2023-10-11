import time
from threading import Thread

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:

        trajeto += velocidade
        time.sleep(0.5)
        print(f'Carro: {piloto} km: {trajeto}')


t_carro1 = Thread(target=carro, args=[1, 'Laisson'])
t_carro2 = Thread(target=carro, args=[2, 'Bruno'])

t_carro1.start()
t_carro2.start()