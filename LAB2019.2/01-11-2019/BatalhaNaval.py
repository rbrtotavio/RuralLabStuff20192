def acharbarco(matriz, posição, tamanho):
    vizinhos = [(posição[0],posição[1])]
    while vizinhos != []:
        aux = vizinhos.pop(0)
        if matriz[aux[0]][aux[1]] != '/':
            if matriz[aux[0]][aux[1]] is '#':
                coor.append(aux)
                matriz[aux[0]][aux[1]] = '/'
                if aux[0] + 1 <= tamanho[0] - 1:
                    acharbarco(matriz, (aux[0] + 1, aux[1]), tamanho)
                if aux[0] - 1 >= 0:
                    acharbarco(matriz, (aux[0] - 1, aux[1]), tamanho)
                if aux[1] + 1 <= tamanho[1] - 1:
                    acharbarco(matriz, (aux[0], aux[1] + 1), tamanho)
                if aux[1] - 1 >= 0:
                    acharbarco(matriz, (aux[0], aux[1] - 1), tamanho)
    return matriz


def destruidos(tiros, navio, cnt=0):
    barcos = navio
    for i in range(len(barcos)):
        aux = barcos[i]
        for j in range(len(aux)):
            t = aux[0]
            if t in tiros:
                del aux[0]
        barcos[i] = aux
    count = barcos.count([])
    print(count)


def pilhadd(lista, arg, fila=[]):
    fila = lista + [arg]
    return fila


if __name__ == "__main__":
    n, m = map(int, input().split())
    matriz = []
    mtiros = []
    coor = []
    barcos = []
    for j in range(n):
        matriz = pilhadd(matriz, list(str(input())))

    for j in range(n):
        for t in range(m):
            if matriz[j][t] is '#':
                a = acharbarco(matriz, (j,t), (n, m))
                barcos.append(coor)
                coor=[]
                matriz = a

    print(matriz)

    a = int(input())

    for v in range(a):
        p, q = map(int, input().split())
        p -= 1
        q -= 1
        mtiros.append((p,q))
