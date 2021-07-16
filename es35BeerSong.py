'''
Moldoveanu Davide
Beer Song
'''

def Song():
    for k in range(1,99):
        print(f"{100-k} bottles of beer on the wall, {100-k} bottles of beer.\nTake one down and pass it around, {99-k} bottles of beer on the wall.\n")

    print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n")

    print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")


def main():
     Song()
        
if __name__ == "__main__":
    main()