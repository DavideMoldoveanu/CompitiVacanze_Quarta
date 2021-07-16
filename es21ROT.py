'''
Moldoveanu Davide
Rotational Cipher
'''

def funzRot(f,x):
    fApp = ""
    for cnt in range (len(f)):
        if(ord(f[cnt]) + x > ord('z')):
            fApp += chr(96 + (ord(f[cnt]) + x - ord('z')))
        else:
            fApp += chr(ord(f[cnt]) + x)

    return fApp

def main():
    frase = input("Inserisci frase: ")
    x = int(input("Inserisci numero di ROT: "))

    print(funzRot(frase,x))

if __name__ == "__main__":
    main()