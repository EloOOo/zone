Zone
====

Projet d'optimisation avec GLPK: problème d'activation de capteur pour la surveillance de zones.

[énnoncé](https://raw.github.com/Ricain/zone/master/projet-plcapteurs.pdf)

# Import

    import random
    import json
    import sys
    import networkx

# Réalisation

## Partie 1: manipulation des données

La géneration des données du probleme se font dans le fichier **genrator.py**

Ce fichier prend deux arguments:

1. `filename` (obligatoire) correspond au nom du fichier dans le quelle seront suavegardé les données generés.
2. `seed` (optionelle) correspond à la "graine" du generateur du nombre aleatoire.

## Partie 2: construction des configurations élémentaire
