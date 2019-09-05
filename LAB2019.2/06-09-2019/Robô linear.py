entrada = input("Digite uma sequências de 'F'(um metro pra frente) e/ou 'T'(um metro pra trás):").upper()    #Aqui transformo a entrada numa string onde todos os componentes são maíusculos

while 'F' in entrada and 'T' in entrada:                                #Aqui eu subistituo cada valor que seja efetivamente nulo para a contagem em um loop
    entrada = entrada.replace('FT', '')                                 #que só permitira que a direção que esteja em maior quantidade permaneça ou que nenhuma
    entrada = entrada.replace('TF', '')                                 #direção permaneça.

if 'F' in entrada:
    print('\nO robô andou', entrada.count('F'), 'metros pra frente!')   #Aqui estabeleço as condições para cada tipo de resultado e, ao fim, contando as direções
elif 'T' in entrada:                                                    #Que sobraram.
    print('\nO robô andou', entrada.count('T'), 'metros pra trás!')
else:
    print("O robô não saiu de sua posição inicial!")