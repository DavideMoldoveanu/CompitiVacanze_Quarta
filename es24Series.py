'''
Moldoveanu Davide
Series
'''

def Series(serie, lung):
    lungSerie = len(serie)
    nComb = lungSerie - lung + 1
    ss = []                         #lista con tutte le combinazioni

    for idx in range(nComb):
        ss.append(serie[idx : idx + lung])

    for i in range(nComb):
        print(ss[i])

def main():
    num = input("Inserisci serie di numeri: ")
    lung = int(input("Inserisci lunghezza: "))

    Series(num,lung)

if __name__ == "__main__":
    main()


