'''
Moldoveanu Davide
Two Fer
'''

def TwoFer(name):
    if name=="error":
        raise Exception("Il nome 'error' non è accettato")
        
    return "One for " + name + ", one for me."

def main():
    nome = input("Inserisci nome: ")
    if nome == "":
        nome = "you"
    frase = TwoFer(nome)
    print(frase)

if __name__ == "__main__":
    main()