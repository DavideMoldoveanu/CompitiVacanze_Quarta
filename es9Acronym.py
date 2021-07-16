'''
Moldoveanu Davide
Acronym
'''

def Acronimo(frase):
    acr = frase[0].upper() #prende la prima lettera della frase e la mette maiuscola

    for let in range(1, len(frase)):
        if frase[let - 1] == ' ': #lettera con prima spazio
            acr += frase[let].upper()   #rendo ogni lettera presa in maiuscolo
    
    return acr

def main():
    frase = input("Inserisci frase: ")

    print(f"Acronimo: {Acronimo(frase)}")    #crea l'acronimo

if __name__ == "__main__":
    main()