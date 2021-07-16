'''
Moldoveanu Davide
Flatten Array --> Prendi un elenco nidificato e restituisci un singolo elenco appiattito con tutti i valori tranne nil/null.
'''

def Flatten(iterable):
    correct = []
    for i in range(len(iterable)):

        if (isinstance(iterable[i], list)):
            correct.extend(Flatten(iterable[i]))      #se c'è una lista dentro un'altra lista richiamo la funzione

        if (isinstance(iterable[i], int)):       #verifico se è un int
            correct.append(iterable[i])

    return correct



def main():

    lst = []
    

    n = int(input("Numero di elementi per lista esterna: "))           #numero di elementi dell futura lista

    for _ in range(0, n):                                   #chiedo in input 
        ris = input("Vuoi un'alra sotto lista? \nS -> si\nN -> no\n")
        if(ris == 'S' or ris == 's'):
            lst1 = []                                       #dichiaro qui la lista perché così si pulisce ogni volta
            n1 = int(input("Numero di elementi per lista interna: "))
            for _ in range(0, n1):
                ele = input("Inserisci numero o 'null': ")
                if ele.strip().isdigit():                       #verifico se è una stringa o un numero
                    ele = int(ele)

                lst1.append(ele)
            lst.append(lst1)
        else:
            ele = input("Inserisci numero o 'null': ")
            if ele.strip().isdigit():
                ele = int(ele)
            lst.append(ele)                                     #aggiungo il valore di input alla lista

    print(Flatten(lst))

if __name__ == "__main__":
    main()