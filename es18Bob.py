'''
Moldoveanu Davide
Bob
'''

yellLett = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','.']

def Bob(frase):

    isUrlo = False              #controllo per le lettere maiuscole
    nomeBob = False             #controllo se è il suo nome

    for lett in frase:
        if lett in yellLett:         #controllo se ci sono yell Letter nella frase scritta
            isUrlo = True
            break

    if frase == 'bob' or frase == 'Bob' or frase == 'bOb' or frase == 'boB' or frase == 'BOb' or frase == 'bOB' or frase == 'BoB' or frase == 'BOB':
        print("Fine. Be that way!")
        nomeBob = True

    if isUrlo == True and nomeBob  == False:              #se yell phrase 
        if frase[-1] == '?':        #controllo se è una yell question
            print("Calm down, I know what I'm doing!")
        else:
            print("Whoa, chill out!")

    elif frase[-1] == '?':          #se la frase è solo una domanda
        print("Sure.")
    elif nomeBob == False:
        print("Whatever.")


def main():

    while True:
        frase = input("Parla con BOB, se non vuoi più parlare con lui scrivi 'STOP': ")
        if frase == 'stop' or frase == 'STOP':        #fine conversazione con BOB
            print("Finish conversation.")
            break
        else:
            Bob(frase)

if __name__ == "__main__":
    main()