'''
Moldoveanu Davide
High Score
'''


def top3(list):
    tupl = [max(list)]
    list.remove(max(list))
    while len(tupl) < 3:
        tupl.append(max(list))
        list.remove(max(list))

    return (tupl[0], tupl[1], tupl[2])


def HighScore(rankList):
    return [max(rankList), rankList[-1], top3(rankList)]


def main():
    listaPunt = []
    cnt = 0
    while cnt < 10:
        punt = int(input("Inserisci un punteggio: "))
        listaPunt.append(punt)
        cnt += 1

    print(f"{HighScore(listaPunt)}")

if __name__ == "__main__":
    main()