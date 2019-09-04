def welsh_powell(grafo):                                                            #Aqui defino a função que aplicará o algoritimo Welsh-Powell
    pontos = sorted(list(grafo.keys()), key=lambda x: len(grafo[x]), reverse=True)  #Nesta linha organizo cada vértice de acordo com sua quantidade de
    cor_mapa = {}                                                                   #arestas de forma decrescente, já que o algoritimo precisa que as vertices
                                                                                    #estejam organizadas de tal forma.
    for ponto in pontos:                                #Aqui ponho em pratica o algoritimo, primeiramente estabelecendo
        cor_disp = [True] * len(pontos)                 #O pior caso: Cada vértice precisar de uma cor distinta. E então
        for vizinho in grafo[ponto]:                    #estabeleco que para cada vizinho haja um índice de preenchimento
            if vizinho in cor_mapa:                     #de suas cores(de 0 à n, sendo 0 uma primeira cor hipotética).
                cor = cor_mapa[vizinho]                 #Cada vértice é uma chave em um dicionario e cada indice é um valor.
                cor_disp[cor] = False                   #cor_disp guarda o valor booleano para verificar se a cor selecionada
        for cor, disponivel in enumerate(cor_disp):     #para certa aresta está disponível para a mesma ou não.
            if disponivel:                              #Se disponível, a função será concluida e repetida até o fim das arestas,
                cor_mapa[ponto] = cor                   #se indisponível um novo índice da ordem de preenchimento será aplicado.
                break

    return cor_mapa                                     #esta função retorna cada vértice(chave) e seus respectivos índices de cor(valor).


if __name__ == "__main__":
    grafo = {'h':{'e', 'f', 'g', 'c', 'd'},
             'g':{'f', 'b', 'c', 'h'},
             'f':{'e', 'b', 'g', 'h'},
             'e':{'a', 'b', 'f', 'h'},
             'd':{'c', 'h'},
             'c':{'b', 'g', 'h', 'd'},
             'b':{'a', 'e', 'f', 'g', 'c'},
             'a':{'b', 'e'}}

print(welsh_powell(grafo))

cores = list(welsh_powell(grafo).values())              #Aqui eu tomo os índices atribuidos ao dicionário, e então,
cores = list(dict.fromkeys(cores))                      #removo as repetições para contar quantas cores foram usadas
qtd_cores = len(cores)                                  #para colorir o mapa.

print("O Mapa precisa de, no mínimo, {} cores!" .format(qtd_cores))
