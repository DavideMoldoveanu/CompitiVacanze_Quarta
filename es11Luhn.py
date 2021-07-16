'''
Moldoveanu Davide
Luhn
'''


def checkLuhn(cardNo):
     
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
  
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False
 

def main():

    cardNo = input("Inserisci: ")

    nCaratteri = 0
    cifreCard = []

    for car in cardNo:
        if car != ' ':
            nCaratteri += 1
            cifreCard.append(car)

    if nCaratteri != 16:                    #verifico se ci sono efettivamente solo 10 caratteri
        print("Codice card non valido")
    else:
        if (checkLuhn(cifreCard)):
            print("Codice card valido")
        else:
            print("Codice card non valido")


if __name__ == "__main__":
    main()