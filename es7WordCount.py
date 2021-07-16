'''
Moldoveanu Davide
Word Count
'''

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            '0','1','2','3','4','5','6','7','8','9']

dizValParola = {}

def ContaParole(frase):
    
    for parola in frase:
        #metto tutte le lettere della frase in maiuscolo così non devo fare un alfabeto enorme e controllo fino alla penultima lettera perché possono esserci lettere accentate o punti e così non devo implementare tutte le casistiche nell'alfabeto
        if parola[-1].upper() not in alfabeto:   
            parola = parola[:-1]
        
        if parola not in dizValParola:
            dizValParola[parola] = 1        #parola inserita con valore pari a 1 se non già presente
        else:
            dizValParola[parola] += 1    #il suo valore viene incrementato se già presente

    return dizValParola

def main():
    str_ = input("Inserisci frase: ")

    str_ = str_.split(" ")              #splitto già la frase

    print(ContaParole(str_))

if __name__ == "__main__":
    main()