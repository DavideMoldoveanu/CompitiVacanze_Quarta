'''
Moldoveanu Davide
Run Leght Encoding
'''

import collections


def RunLeght(string):

    cnt = collections.OrderedDict.fromkeys(string, 0)       #uso libreria importata

    for char in string:
        cnt[char] += 1

    encodedString = ""

    for key, value in cnt.items():
        encodedString += key + str(value)
    
    print(encodedString)


def main():
    string = input("Insersci una stringa: ")
    RunLeght(string)

if __name__ == "__main__":
    main()

