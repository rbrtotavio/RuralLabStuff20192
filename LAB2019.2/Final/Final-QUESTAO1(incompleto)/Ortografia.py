def editarpalavra(a, b):
    tabela = []
    tabela = tabela + [i for i in range(len(b)+1)] #estava tentando procurar uma maneira de subistituir as letras entre duas palavras com tamanhos parecidos
    for i in range(1, len(a) + 1):
        tabela = tabela + []
        for j in range(len(b) + 1):

if __name__ == "__main__":
    dicionario = []
    entradas = []
    n, m = input().split()
    for i in range(int(n)):
        dicionario = dicionario + [input()]
    for j in range(int(m)):
        entradas = entradas + [input()]
    for entradas in entradas:
        for palavra in dicionario:
