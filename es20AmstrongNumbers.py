'''
Moldoveanu Davide
Amstrong Numbers
'''

def nCifre(x):          #mi dice quante cifre ha il numero inserito
    ctn = 0
    while (x != 0):
        ctn = ctn + 1
        x = x // 10     #floor division
          
    return ctn
  
def isArmstrong(x):
        
    n = nCifre(x)
    print(n)
    temp = x
    somma = 0
      
    while (temp != 0):
        r = temp % 10
        somma = somma + r**n
        temp = temp // 10
  
    # If condition satisfies
    return (somma == x)


def main():
    x = int(input("Inserisci un numero: "))
    print(isArmstrong(x))

if __name__ == "__main__":
    main()

