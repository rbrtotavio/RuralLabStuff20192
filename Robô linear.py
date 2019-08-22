entrada = input("").upper()

while 'F' in entrada and 'T' in entrada:
    entrada = entrada.replace('FT', '')
    entrada = entrada.replace('TF', '')

if 'F' in entrada:
    print('\nO robô andou', entrada.count('F'), 'metros pra frente')
else:
    print('\nO robô andou', entrada.count('T'), 'metros pra trás')