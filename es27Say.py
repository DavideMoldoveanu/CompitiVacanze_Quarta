'''
Moldoveanu Davide
Say
'''


def Converti(num):
 
    l = len(num)

    if (l == 0):
        print("Stringa vuota")
        return

     
    if (l > 4):
        print("Lunghezze superiore a 4 non sono sopportate")
        return
 
    cifreSingole = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]


    cifreDoppie = ["", "ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]
 

    multipliDieci = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty",
                     "ninety"]
 
    potenzeDieci = ["hundred", "thousand"]
 
    print(f"{num}:", end=" ")
 
    #gestisco numeri a cifra singola
    if (l == 1):
        print(cifreSingole[ord(num[0]) - 48])      #restituisce un numero intero che rappresenta il valore in codice Unicode
        return
 
    x = 0
    while (x < len(num)):       #gestisco cifra per cifra
 
        #se più di 2 cifre (ovvero numeri con 3 e 4 cifre)
        if (l >= 3):
            if (ord(num[x]) - 48 != 0): 
                print(cifreSingole[ord(num[x]) - 48], end=" ")     #mette alla fine uno spazio e non un acapo
                print(potenzeDieci[l - 3], end=" ")                   #facccio l-3 perché se sono 4 cifre 4-3 fa 1 e perciò sara "thousand", se sono 3 le cifre 3-3 fa 0 e perciò hundred
 
            l -= 1
        #se numeri con solo 2 cifre
        else:
            #gestisco esplicitamente 10-19. La somma delle due cifre viene utilizzata come indice di un array di stringhe a "cifreDoppie"
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 + ord(num[x+1]) - 48)
                print(cifreDoppie[sum])
                return
 
            #gestisco esplicitamente 20
            elif (ord(num[x]) - 48 == 2 and ord(num[x + 1]) - 48 == 0):
                print("twenty")
                return
 
            #numeri da 21 a 99
            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    print(multipliDieci[i], end=" ")
                else:
                    print("", end="")
                x += 1
                if(ord(num[x]) - 48 != 0):
                    print(cifreSingole[ord(num[x]) - 48])
        x += 1
 
 

def main():
    n = input("Inserisci numero con massimo 4 cifre: ")
    Converti(n)

if __name__ == "__main__":
    main()