'''
Moldoveanu Davide
Prime Factors
'''

from math import sqrt       #facendo così posso usare solo sqrt() invece se importavo tutto math potevo usare tutti i metodi

def PrimeFactors(n):
     
    #Stampa il numero di due che dividono n
    while n % 2 == 0:
        print(f"Il numero {n} è divisibile per 2")
        n = int(n / 2)                      #li casto a int perché so che sono interi e così nella stampa sarà più ordinato
         
    #n ora è dispari, quindi ora incremento di 2 ( i = i + 2)
    for i in range(3, int(sqrt(n))+1, 2):            #parto da 3 perché appunto il 2 l'abbiamo già verificato e vado fino all'intero della radice di n
         
        #se n mod i da 0 allora stampo i, perché significa che è divisibile
        while n % i == 0:
            print(f"Il numero {n} è divisibile per {i}")
            n = int(n / i)       #divido il numero perché appunto mi dà un numero intero
             
    #se n è un primo sarà sicuramente maggiore di 2
    if n > 2:
        print(f"Il numero {n} è divisibile per {n}")


 


def main():
    n = int(input("Inserisci numero: "))
    PrimeFactors(n)

if __name__ == "__main__":
    main()