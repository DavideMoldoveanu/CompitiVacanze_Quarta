'''
Moldoveanu Davide
Clock
'''

days = ['Lundì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
clock = {'Giorno': days[0], 'Ore': 0, 'Minuti':0}       #diz

def Clock(nMin, decision, gg):

    if decision == 'a' or decision == 'A':
        clock['Minuti'] += nMin                      
        while clock['Minuti'] >= 60:                   #metto while, così anche se metto 120 min lo eseguo più volte (controlla i minuti e di conseguenza le ore)
            clock['Ore'] += 1
            clock['Minuti'] -= 60                      #decremento i min di 60 min perché aggiungo incremento le ore (clock['Minuti'] fa anche da contatore)

        while clock['Ore'] >= 24:                      #controlla le ore e di conseguenza i giorni
            gg += 1     
            if gg < len(days):
                clock['Giorno'] = days[Giorno]
            else:          
                Giorno = 0
                clock['Giorno'] = days[Giorno]
            
            clock['Ore'] -= 24      
    
    else:                                           #diminuzione minuti, stessa logica dell'aumento di minuti
        clock['Minuti'] -= nMin
        while clock['Minuti'] < 0:
            clock['Ore'] -= 1
            clock['Minuti'] += 60
        
        while clock['Ore'] < 0:
            gg -= 1
            if gg >= 0:
                clock['Giorno'] = days[gg]
            else:
                gg = len(days)-1 
                clock['Giorno'] = days[gg]
            
            clock['Ore'] += 24
    
    print(clock)

    return gg


def main():

    day = 0

    while True:
        decision = input("A --> Aumenta, D --> Diminuisce, S --> Stop: ")

        if decision != 'A' and  decision != 'a' and  decision != 'D' and  decision != 'd' and decision != 'S' and decision != 's':      #controllo scelta aum/dic/stop
            print("Lettera inesistente, sarà scelto in automatico di aumentare")
            decision = 'A'
            nMin = int(input("Di quando vuoi aumentare (minuti)? "))
        elif decision == 'A' or  decision == 'a':
            nMin = int(input("Di quando vuoi aumentare (minuti)? "))
        elif decision == 'D' or  decision == 'd':
            nMin = int(input("Di quando vuoi diminuire (minuti)? "))
        elif decision == 'S' or decision == 's':
            print("Arresto esecuzione")
            break
        
        if nMin < 0:                                                             #controllo valore aum/dic
            print("Numero selezionato inesistente, sarà scelto in automatico di aumentare di 10 minuti")
            nMin = 10
        
        day = Clock(nMin, decision, day)

if __name__ == "__main__":
    main()