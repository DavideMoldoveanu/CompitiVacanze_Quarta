'''
Moldoveanu Davide
Raindrops
'''

def CreateString(n):
    string = ''

    #creo la stringa ma prima controllo se il numero è un multiplo di 3, 5 e 7
    if n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        string = n
    else:
        if n % 3 == 0:
            string += 'Pling'
        if n % 5 == 0:
            string += 'Plang'
        if n % 7 == 0:
            string += 'Plong'
    
    return string


def main():
    num = int(input("Inserisci numero: "))      #faccio già subito il casting
    print(CreateString(num))

if __name__ == "__main__":
    main()