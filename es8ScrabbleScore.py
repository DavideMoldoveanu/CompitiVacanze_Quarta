'''
Moldoveanu Davide
Scrabble Score
'''

letVal = {'AEIOULNRST' : 1, 'DG' : 2, 'BCMP' : 3, 'FHVWY' : 4, 'K' : 5, 'JX' : 8, 'QZ' : 10}  #dizionario con i valori delle lettere (metto tutto in UPPERCASE così non devo scrivere tutte le lettere sia in maiuscolo che in minuscolo)


def scrabbleScore(frase):
    punt = 0   

    for let in frase:    
        for string, val in letVal.items():        #prendo "item" del dizionario
            for lettera in string:                  #ciclo dentro all'item
                if lettera == let.upper():       #metto in caps e vedo se il carattere della frase c'è nel diz
                    punt += val
    
    return punt
            

def main():
    frase = input("Inserisci frase: ")
    print(f"Punteggio totale: {scrabbleScore(frase)}")

if __name__ == "__main__":
    main()