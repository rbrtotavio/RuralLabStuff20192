import sys

sys.setrecursionlimit(1000000)


def acharcampo(matriz, posicao, tamanho):
    vizinhos = [(posicao[0],posicao[1])]
    global coor
    while vizinhos != []:
        aux = vizinhos.pop(0)
        if matriz[aux[0]][aux[1]] != '/' or matriz[aux[0]][aux[1]] != '#':
            if matriz[aux[0]][aux[1]] == 'v' or matriz[aux[0]][aux[1]] == 'k' or matriz[aux[0]][aux[1]] == '.':
                coor.append(matriz[aux[0]][aux[1]])
                matriz[aux[0]][aux[1]] = '/'
                if aux[0] + 1 <= tamanho[0] - 1:
                    acharcampo(matriz, (aux[0] + 1, aux[1]), tamanho)
                if aux[0] - 1 >= 0:
                    acharcampo(matriz, (aux[0] - 1, aux[1]), tamanho)
                if aux[1] + 1 <= tamanho[1] - 1:
                    acharcampo(matriz, (aux[0], aux[1] + 1), tamanho)
                if aux[1] - 1 >= 0:
                    acharcampo(matriz, (aux[0], aux[1] - 1), tamanho)
    return matriz


def contarlobosovelhas(campo, cntv=0, cntk=0):
    fazenda = campo
    animais = []
    for i in range(len(fazenda)):
        if '.' in fazenda[i]:
            aux = fazenda[i].remove('.')
        if fazenda[i] != None:
            cv = fazenda[i].count('v')
            ck = fazenda[i].count('k')
            if cv >= ck:
                cntv += cv
            else:
                cntk += ck
    print(cntk, cntv)


def pilhadd(lista, arg, fila=[]):
    fila = lista + [arg]
    return fila


if __name__ == "__main__":
    n, m = map(int, input().split())
    matriz = []
    campos = []
    coor = []
    for j in range(n):
        matriz = pilhadd(matriz, list(str(input())))


    for j in range(n):
        for t in range(m):
            if matriz[j][t] == '.' or matriz[j][t] == 'v' or matriz[j][t] == 'k':
                a = acharcampo(matriz, (j,t), (n, m))
                campos.append(coor)
                coor=[]
                matriz = a

    contarlobosovelhas(campos)