'''
Moldoveanu Davide
ISBN Verifier
'''

caratteriAcettati = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']     #X --> 10

def validISBN(numberList):
    somma = 0

    for k in range(0, 10):
        somma += numberList[k] * (10-k)     #prima parte della formula

    if somma % 11 == 0:                 #verifico se la somma è divisibile per 11 (seconda parte della formula)
        print("SI ISBN-10")
    else:
        print("NO ISBN-10")
        

def main():
    isbn = input("Inserisci ISBN-10: ").upper()       #lo metto già subito in caps perché si potrebbe scrivere la 'x' in minuscolo

    nCaratteri = 0
    cifreISBN = []

    for car in isbn:
        if car != '-':
            if car in caratteriAcettati:
                nCaratteri += 1
                if car == 'X':
                    cifreISBN.append(10)
                else:
                    cifreISBN.append(int(car))
            else:
                print("Codice ISBN-10 non valido.")
                break
                
    
    if nCaratteri != 10:                    #verifico se ci sono efettivamente solo 10 caratteri
        print("Codice ISBN-10 non valido.")
    else:
        validISBN(cifreISBN)

if __name__ == "__main__":
    main()

