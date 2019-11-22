def acharcaminho(grafo, comeco, fim, caminho=[]):
    caminho = caminho + [comeco]
    if comeco == fim:
        return len(caminho) - 1
    else:
        for cidade in grafo[comeco - 1]:
            if cidade not in caminho:
                rota = acharcaminho(grafo, cidade, fim, caminho)
                if rota:
                    return rota


if __name__ == "__main__":
    n, a, b = map(int, input().split())
    grafo = [[] for x in range(n)]
    for j in range(n - 1):
        p, q = map(int, input().split())
        grafo[p - 1] = grafo[p - 1] + [q]
        grafo[q - 1] = grafo[q - 1] + [p]
    print(acharcaminho(grafo, a, b))
