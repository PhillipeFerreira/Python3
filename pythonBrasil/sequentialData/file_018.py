downl = float(input('Tamanho do arquivo(MB): '))
vel_web1 = float(input('Velocidade da internet(Mbps): '))
vel_web2 = vel_web1/0.125

time = (downl/vel_web2)

print(f'Tempo para baixar: {time} minutos')
