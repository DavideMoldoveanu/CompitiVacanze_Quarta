'''
Moldoveanu Davide
RNA Transcription
'''

def transcript(x) :

    l = list(x)  
  
    for i in range(len(x)):

        if(l[i]=='G'):
            l[i]='C'

        elif(l[i]=='C'):
            l[i]='G'

        elif (l[i] == 'T'):
            l[i] = 'A'

        elif (l[i] == 'A'):
            l[i] = 'U'

        else:
            print('DNA INVALID')
   
   
    print("DNA TRASLATO: ",end="")     #con queste 3 righe di codice faccio in modo che il contenuto della lista 'l' sia stampato senza virgolette e parentesi quadre
    for char in l:
        print(char,end="")

def main():

    x = input("Inserisci DNA: ")

    transcript(x)

if __name__ == "__main__":
    main()