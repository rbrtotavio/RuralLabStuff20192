def doislacos(string):
    z = len(string)
    for i in range(z):
        for j in range(0, z):
            if i <= j:
                print(string[i : j + 1])


def umlaco(string):
    z = len(string)
    i = 0
    j = 0
    while i <= z:
        if j == z:
            i += 1
            j = i
        j += 1
        if string[i : j] == "":
            break
        else:
            print(string[i : j])


def recursivo(string, i=0, j=1):
    if i > len(string):
        return None
    elif j > len(string):
        recursivo(string, i + 1, i)
        return None
    elif string[i : j] != None:
        if i < j:
            print(string[i : j])
        recursivo(string, i, j + 1)


entrada = "Paula"
doislacos(entrada)
print('\n' +("_-" * 40) +'\n')
umlaco(entrada)
print('\n' +("_-" * 40) +'\n')
recursivo(entrada)