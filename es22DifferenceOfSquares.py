'''
Moldoveanu Davide
Difference Of Squares
'''


def Quadrati(n):
    quadSomma = 0
    sommaQuad = 0

    i = 1           #così parte a sommare da 1 e non da 0

    for i in range(n+1):
        quadSomma += i    #somma dei numeri minori della soglia

    quadSomma = quadSomma ** 2  

    i = 1       #così parte a fare i quadrati dei numeri da 1 e non da 0

    for i in range(n+1):
        sommaQuad = sommaQuad + i ** 2 

    return quadSomma-sommaQuad  


def main():
    num = int(input("Inserisci una soglia positiva: "))

    if num <= 0:
        print("Numeri negativi o 0 non sono accettati, perciò in automatico verrà messo 10!")
        num = 10

    differenza = Quadrati(num)

    print(f"Differenza tra il quadrato della somma dei primi {num} numeri e la somma dei primi {num} numeri al quadrato: {differenza}") 


if __name__ == "__main__":
    main()