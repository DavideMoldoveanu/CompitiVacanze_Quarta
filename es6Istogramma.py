'''
Moldoveanu Davide
Istogramms
'''

def IsIstogramma(word):
    listaLett = []
    isIst = True

    for lett in word.upper():
        if lett in listaLett and lett != ' ' and lett != '-':   #controllo se la lettera è ripetuta e che non sia uno spazio o un "-"
            isIst = False   #no isogramma
            break

        listaLett.append(lett)
    
    if isIst == True:
        print(f"{word} è un isogramma")
    else:
        print(f"{word} non è un isogramma")


def main():
    word = input("Inserisci parola: ")
    IsIstogramma(word)


if __name__ == "__main__":
    main()