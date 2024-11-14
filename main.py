""" Calcule et vérifie si un nombre est premier ou pas
"""
from math import sqrt

#### Fonction secondaire
def isprime(p):
    """ Indique si le nombre entier entré est premier.
    Args : 
        p : Valeur entière positive
    Returns :
        isprime(p) : True
    """

    premier = True
    if p in (1,0) :
        premier = False
    for k in range(2,int(sqrt(p))+1):
        if p%k == 0:
            premier = False
            break
    return premier

#### Fonction principale
def main():
    """ Fait appel à la fonction secondaire et vérifie son bon fonctionnement
    Args :
        none
    Returns : 
        none
    """

    print(isprime(0), isprime(1), isprime(2), isprime(43))

    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()
