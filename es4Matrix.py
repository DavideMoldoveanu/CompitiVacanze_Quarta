'''
Moldoveanu Davide
Matrix

non del tutto corretto
'''

import numpy as np


def main():
    nY = int(input("Inserisci il numero di colonne: "))
    nX = int(input("Inserisci il numero di righe: "))

    mat = np.arange(1,nX*nY+1).reshape((nX, nY))

    print(mat)

    print(f"Numero righe e colonne: {mat.shape}")


if __name__ == "__main__":
    main()