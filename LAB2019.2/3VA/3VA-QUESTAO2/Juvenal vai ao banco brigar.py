if __name__ == '__main__':

    t = int(input())
    for i in range(t):
        n = int(input())
        regular = []
        preferencial = []
        print("Caso {}:".format(i + 1))
        for j in range(n):
            comando = input()
            if comando == "I":
                if regular:
                    print(regular[0] ,' ', end='')
                else:
                    print(0, ' ', end='')
                if preferencial:
                    print(preferencial[0])
                else:
                    print(0)
            elif comando == "A":
                if regular:
                    regular.remove(regular[0])
                elif not regular and preferencial:
                    preferencial.remove(preferencial[0])
            elif comando == "B":
                if preferencial:
                    preferencial.remove(preferencial[0])
                elif not preferencial and regular:
                    regular.remove(regular[0])
            else:
                instrucao = [i for i in comando]
                if instrucao[0] == "f":
                    regular = regular + [int(instrucao[2])]
                else:
                    preferencial = preferencial + [int(instrucao[2])]