'''
Moldoveanu Davide
Space Age
'''

planets = {'Mercury':0.2408467, 'Venus':0.61519726, 'Mars':1.8808158, 'Jupiter':11.862615, 'Saturn':29.447498,
           'Uranus':84.016846, 'Neptune':164.79132}

earth_orbital_period = 86400 * 365.25       #31.557.600


def CalculateAge(second):
    for planet in planets:
        age =round(earth_orbital_period * planets[planet], 2)
        print(f"On {planet} you're {age} years old: ")          #arrotondato alla seconda cifra dopo la virgola

def main():
    seconds = int(input("Inserisci età in secondi: "))
    if seconds < 0:
        print("Età inesistente, verrà selezionato automaticamente 1 secondo!!")
        CalculateAge(seconds)
    else:
        CalculateAge(seconds)

if __name__ == "__main__":
    main()