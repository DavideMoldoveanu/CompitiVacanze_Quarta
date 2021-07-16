'''
Moldoveanu Davide
Hamming Distance
'''

def hammingDistance(string1, string2):
	distanza = 0
	for n in range(len(string1)):
		if string1[n] != string2[n]:
			distanza += 1
	return distanza


def main():
    dna1 = input("Insersci il primo DNA: ")
    dna2 = input("Inserisci il secondo DNA: ")

    distanza = hammingDistance(dna1, dna2)

    print(f"La distanza tra i due DNA è di {distanza}")


if __name__ == "__main__":
    main()