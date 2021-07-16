'''
Moldoveanu Davide
Series
'''

def SieveOfEratosthenes(n):

    prime = [True for i in range(n + 1)]    #metto tutti i numeri della lista a True
    p = 2
    while (p * p <= n):
        if (prime[p] == True):          #se prime[p] non è cambiato allora sarà un numero primo
            #aggiorno tutti i multipli di p a False
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    prime[0]= False     #contiene il numeo 0, ma i numeri devono essere stampati partendo da 2, perciò mettiamo il loro valore a False e poi nella stampa non saranno presenti
    prime[1]= False     #contiene il numeo 1, ma i numeri devono essere stampati partendo da 2, perciò mettiamo il loro valore a False e poi nella stampa non saranno presenti

    #stampo i numeri primi
    for p in range(n + 1):
        if prime[p] == True:
            print (p)

def main():
    n = int(input("Inserisci limite: "))
    print(f"I numeri primi minori o uguali a {n}:") 
    SieveOfEratosthenes(n)

if __name__ == "__main__":
    main()