def PythagoreanTriplet(n):
    nList = [k for k in range(1, n)]  #metto tutti i numeri da 1 a n
    pytTripList =  []

    #tripo ciclo solo per poter poi fare la somma nell if
    for a in nList:
        for b in range(a+1, len(nList)+1, 1):
            for c in range(b+1, len(nList)+1, 1):
                if a+b+c == n and a**2 + b**2 == c**2:      #a < b < c --> sempre vera perché sono 3 cicli concatenati
                    pytTripList.append([a,b,c])     #inserirsco più liste dentro a una lista perché così se ci sono più triplette sono separate
    
    return(pytTripList)


def main():
    ret = []
    num = int(input("Inserisci un numero: "))

    ret = PythagoreanTriplet(num)

    for i in range(len(ret)):
        print(*ret[i],sep=", ")     #stampo senza virgolette (in caso di stringhe) e senza quadre
    
if __name__ == "__main__":
    main()