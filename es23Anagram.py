

def Anagram(parola,candidati):
    nCand = len(candidati)
    k = 0

    while k < nCand:
        if sorted(parola) == sorted(candidati[k]):                  #posso usare anche Counter() (importanto --> from collections import Counter) questo è possibile farlo da python3 in avanti
            print(f"La parola {candidati[k]} è un anagramma")
        else:
            print(f"La parola {candidati[k]} non è un anagramma")
        k += 1
    

def main():

    str_ = input("Inserisci parola: ")
    candidati = []
    
    while True:
        agg = int(input("Inserisci 0 per uscire e 1 per aggiungere un candidato: "))

        if agg == 1:
            candidato = input(f"Inserisci un cadidato per {str_}: ")
            candidati.append(candidato)
        else:
            print("Andiamo a cercare se c'è qualche anagramma!")
            break       

    Anagram(str_,candidati)


if __name__ == "__main__":
    main()