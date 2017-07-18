#!/usr/bin/python3
# -*-coding:Utf-8 -*

import random
import math

# Saisie des conditions initiales
try:
    somme=input("Saisissez votre somme initial :")
    somme=int(somme)
except:
    somme=input("Vous n'avez pas saisi un nombre adéquate, saisissez votre somme initial :")
    somme=int(somme)


# boucle sur le calcul et la saisie des mises
while somme!=0: 
 
    # saisie du numero parie
    numero_mise=0
    while numero_mise <= 0 or numero_mise > 49:
        try: 
            numero_mise=input("Saisissez le numéro sur lequel vous misez entre 0 et 49: ")
            numero_mise=int(numero_mise)
        except:
            numero_mise=input("Vous n'avez pas saisi un nombre adéquate, saisissez le numéro sur lequel vous misez entre 0 et 49: ")
            numero_mise=int(numero_mise)
    # saisie des mises
    try:
        montant_mise=input("Saisissez le montan de votre mise :")
        montant_mise=int(montant_mise)
    except:    
        montant_mise=input("Vous n'avez pas saisi un nombre adéquate, saisissez le montan de votre mise :")
        montant_mise=int(montant_mise)

    while montant_mise>somme:
        montant_mise=input("Le montant saisi est supérieur à votre somme, saisissez un montant inférieur :")
        montant_mise=int(montant_mise)

    # tirage au sort, verification des conditions et calcul des gains et pertes 
    tirage=random.randrange(50)
    if numero_mise==tirage: 
        gain=montant_mise*3
    elif numero_mise%2==0 and tirage%2==0:
        gain=montant_mise/2
    elif numero_mise%2!=0 and tirage%2!=0:
        gain=montant_mise/2
    else: 
        gain=-montant_mise
    gain=math.ceil(gain)    
    somme=somme+gain

    # message des résultats
    message1="Vous avez tirer le numéro : "
    message2=", votre somme total est de "
    print(message1 + str(tirage) + message2 + str(somme))

print("Vous avez perdu tout votre argent ! Vous ferriez mieux de ne pas jouer au casino !")

input("Appuyez sur ENTREE pour fermer ce programme...")

