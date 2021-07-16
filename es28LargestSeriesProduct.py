'''
Moldoveanu Davide
Largest Series Product
'''

from math import prod

def LargestProduct(series, size):
    result = 0

    if size < 0 or size > len(series):
        print("Serie e dimensioni sbagliate")
        return
    elif size == 0:
        result = 1
    elif size <= len(series):
	    for i in range(len(series) - size + 1):             #a una numero di 8 cifre con size di 3, il ciclo sarà eseguito 6 volte
		    result = max(result, prod((int(x) for x in series[i:i + size])))        #sceglie il massimo tra result e il prodotto di x con x (series[i:i + size] --> da i a i+size)
    
    return result



def main():
    n = input("Inserisci una serie: ")
    size = int(input("Inserisci una size: "))
    print(LargestProduct(n,size))

if __name__ == "__main__":
    main()