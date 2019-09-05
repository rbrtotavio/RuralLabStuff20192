def welsh_powell(grafo):                                                            #Aqui defino a função que aplicará o algoritimo Welsh-Powell
    pontos = sorted(list(grafo.keys()), key=lambda x: len(grafo[x]), reverse=True)  #Nesta linha organizo cada vértice de acordo com sua quantidade de
    cor_mapa = {}                                                                   #arestas de forma decrescente, já que o algoritimo precisa que as vertices
                                                                                    #estejam organizadas de tal forma.
    for ponto in pontos:                                #Começo a aplicar o algoritimo apartir do seu pior caso (uma cor hipotética para cada vértice.
        cor_disp = [True] * len(pontos)                 #Após isso eu verifico se o vizinho do vértice que o programa colorirá já está colorido, pois,
        for vizinho in grafo[ponto]:                    #se o mesmo estiver, o vértice estará como chave no dicionário cor_mapa.
            if vizinho in cor_mapa:                     #Se o vizinho estiver colorido, a cor que o colore não poderá mais ser utilizada (após verificar os outros vizinhos, caso tenha)
                cor = cor_mapa[vizinho]
                cor_disp[cor] = False
        for cor, disponivel in enumerate(cor_disp):     #e se não estiver colorido, sua cor se tornará a cor com o menor índice (já que as cores hipotéticas são números)
            if disponivel:                              #e que seja disponível.
                cor_mapa[ponto] = cor
                break

    return cor_mapa                                     #esta função retorna cada vértice(chave) e seus respectivos índices de cor(valor).

if __name__ == "__main__":

    a = int(input())

    matrix = [[i for i in map(int, input().split(' '))] for x in range(a)]  #Aqui recebo a entrada em forma de matriz, atribuindo os inteiros à uma
                                                                            #Matriz de adjacêcia (como recomendado pelo Monitor da disciplina).
    grafo = {v: [l for l, vizinho in enumerate(fila) if vizinho] for v, fila in enumerate(matrix)} #Aqui pego as filas e as enumero para estabelecer chaves num dicionario
                                                                                                 #sendo cada fileira uma chave (vértice) e cada valor vizinho (1) relaciona
                                                                                                 #estes vértices.
    cores = list(welsh_powell(grafo).values())          # Aqui eu tomo os índices atribuidos ao dicionário, e então,
    cores = list(dict.fromkeys(cores))                  # removo as repetições para contar quantas cores foram usadas
    qtd_cores = len(cores)                              # para colorir o mapa.

    print("O Mapa precisa de, no mínimo, {} cores!".format(qtd_cores))
