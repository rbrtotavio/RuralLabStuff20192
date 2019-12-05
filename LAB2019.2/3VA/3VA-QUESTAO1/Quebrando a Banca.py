def minimo(a):
    m = a[0]
    for item in a:
        if item < m:
            m = item
    return m

def juvenalquerdinheiro(saldoc, b):
    for l in range(int(b)):
        z = minimo(saldoc)
        saldoc.remove(z)
    return saldoc

if __name__ == "__main__":

    while True:
        try:
            a, b = map(int, input().split())
            c = input()
            saldo = []
            if a and b:
                for l in c:
                    saldo = saldo + [int(l)]
                t = juvenalquerdinheiro(saldo, b)
                for j in t:
                    print(j, end="")
                print()
        except ValueError:
            EOFError
            break
