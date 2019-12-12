class AreaNodo:
    def __init__(self, data):
        self.data = data
        self.ant = None
        self.prox = None
        self.devastado = None
        self.visitado = None

class Fazenda:
    def __init__(self, data):
        node = AreaNodo(data)
        self.head = node

def inserirarea(fazenda, numero):
    y = None
    x = fazenda.head
    for i in range(1, numero + 1):
        x.data = i
        y = x
        x = AreaNodo(x.prox)
        x.ant = y
        y.prox = x
        if i == numero:
            y.prox = fazenda.head
            fazenda.head.ant = y
            x = None
    return fazenda

def obliterararea(nodo, k):
    while nodo != None and k != nodo.data:
        nodo = nodo.prox
    nodo.devastado = True

def robocaminhando(nodo, comandos, count=0):
    for comando in comandos:
        nodo.visitado = True
        if nodo.visitado == True and nodo.devastado == True:
            count += 1
        if comando == 1:
            nodo.visitado = None
            nodo = nodo.prox
        elif comando == -1:
            nodo.visitado = None
            nodo = nodo.ant
    if nodo.visitado == None and nodo.devastado == True:
        count += 1
    return count

if __name__ == "__main__":
    n, c, s = input().split()
    fazenda = inserirarea(Fazenda(None), int(n))
    obliterararea(fazenda.head, int(s))
    lista = [int(comando) for comando in input().split()]
    print(robocaminhando(fazenda.head, lista))
