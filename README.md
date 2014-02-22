Zone
====

Projet d'optimisation avec GLPK: problème d'activation de capteur pour la surveillance de zones.

[énnoncé](http://raw.github.com/Ricain/zone/projet-plcapteurs.pdf)

# Import

    import random
    import json
    import sys

# Réalisation

## Partie 1

Géneration des données du probleme: fichier **genrator.py**

Ce fichier prend deux arguments:

1. `filename` (obligatoire) correspond au nom du fichier dans le quelle seront suavegardé les données generés.
2. `seed` (optionelle) correspond à la "graine" du generateur du nombre aleatoire.