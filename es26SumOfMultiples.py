'''
Moldoveanu Davide
Sum Of Multiples
'''

def sum_of_multiples(limit, multiples):
    listaNum = []
    if 0 in multiples:                  #controllo che nella tupla di multipes non ci sia 0, se prensente lo levo
        multiples.remove(0)
    for i in multiples:
        j = 1
        while i * j < limit:            #moltiplico i valori della tupla fino a quando un loro multiplo non supera il limite
            listaNum.append(i * j)      #aggiungo ogni multiplo della tupla
            j += 1
    print(f"Somma dei multipli: {sum(set(listaNum))}")


def main():
    n = int(input("Inserisci limite: "))
    temp = input("Inserisci i multipli separati da una virgola: ")
    lim = tuple(int(x) for x in temp.split(','))
    sum_of_multiples(n,lim)

if __name__ == "__main__":
    main()