def custo(lista, graph, dist=0, count=0):
    while count < len(lista):
        h = graph[lista[0]][lista[1]]
        del lista[0]
        g = lista
        count += 1
        dist = h + custo(g, graph, dist, count)
    return dist

def caminho(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = caminho(graph, node, end, path)

            if newpath: return newpath
    return None

if __name__ == "__main__":

    n, a, b = map(int, input().split())
    grafo = {x + 1: {} for x in range(n)}
    for i in range(n - 1):
        p, q, d = map(int, input().split())
        grafo[q].update(dict({p: d}))
        grafo[p].update(dict({q: d}))

    print(custo(caminho(grafo, a, b), grafo))
