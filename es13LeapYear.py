'''
Moldoveanu Davide
Leap Year

Si Leap Year:
    anno divisibile per 4 o per 4 e 400

No Leap Year:
    anno non divisibile per 4 o divisibile per 4 e per 100
'''

def Leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year}: SI Leap Year")
            else:
                print(f"{year}: NO Leap Year")
        else:
            print(f"{year}: SI Leap Year")
    else:
        print(f"{year}: NO Leap Year")  


def main():
    year = int(input("Inserisci un anno: "))
    Leap(year)


if __name__ == "__main__":
    main()