'''
Moldoveanu Davide
Sublist
'''

def Sublist(list_one, list_two):
    if list_one == list_two:
        return(f"{list_one} uguale a {list_two}")
    elif len(list_one) > len(list_two):
        bigger = list_one
        smaller = list_two
    else:
        bigger = list_two
        smaller = list_one
    for i in range(len(bigger)):
        if bigger[i:i + len(smaller)] == smaller and bigger == list_one:
            return(f"{list_one} è la superlista di {list_two}")
        elif bigger[i:i + len(smaller)] == smaller and bigger == list_two:
            return(f"{list_one} è la sottolista di {list_two}")
    return(f"{list_one} non è superlista, sottolista o uguale a {list_two}")


def main():

    lst_one = []
    lst_two = []
    

    n = int(input("Numero di elementi per la prima lista: "))           #numero di elementi dell futura lista

    for _ in range(0, n):                                   #chiedo in input 
        ele = int(input("Inserisci un numero: "))
        lst_one.append(ele)                                     #aggiungo il valore di input alla lista

    
    n = int(input("Numero di elementi per la seconda lista: "))           #numero di elementi dell futura lista

    for _ in range(0, n):                                   #chiedo in input 
        ele = int(input("Inserisci un numero: "))
        lst_two.append(ele)                                     #aggiungo il valore di input alla lista

    print(Sublist(lst_one,lst_two))

if __name__ == "__main__":
    main()