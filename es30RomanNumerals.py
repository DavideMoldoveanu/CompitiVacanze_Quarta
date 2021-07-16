'''
Moldoveanu Davide
Roman Numerals
'''


def PrintRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    simb = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:                       #come dire x!=0
        div = number // num[i]          #faccio div e vedo parte intera
        #cambio number quando trovo un 'i' che facendo number // num[i] non mi dia 0
        number %= num[i]                #come dire numer = numer % num[i]
 
        #entro in questo while solo quando trovo un numero che non dia a div=0
        while div:
            print(simb[i], end = "")
            div -= 1
        i -= 1
 

def main():
    number = int(input("Inserisci numero decimale: "))
    print("Roman numeral is:", end = " ")
    PrintRoman(number)

if __name__ == "__main__":
    main()