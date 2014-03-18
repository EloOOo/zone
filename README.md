Zone
====

Projet d'optimisation avec GLPK: problème d'activation de capteur pour la surveillance de zones.

[énnoncé](https://raw.github.com/Ricain/zone/master/projet-plcapteurs.pdf) 

# Réalisation

## Partie 1: manipulation des données

La géneration des données du probleme se font dans le fichier **json-gen.py**

Le fichier `exemple.json` correspond à la modelisation des données en exemple dans l'[énnoncé](https://raw.github.com/Ricain/zone/master/projet-plcapteurs.pdf).

### arguments

Ce script prend en paramettre le nom d'un fichier dans le quelle le script sauvegarde les donné generé au format json.

Arguments optionelles: ces options permette de redefinir les constantes du script.

- `-nbcapteur <int>` correspond au nombre de capteur voulu.
- `-zonecoef <float>` plus ce coefficient est bas plus le prgramme aura tendance a cree de nouvl zone pour les capteur, doit etre comprit entre 0 et 1
- `-maxtmp <int>` correspond a maximun de temps d'activation d'un capteur
- `-seed <int>` correspond à la graine du generateur de nombre aleatoire
- `-maxzone <int>` correspond au nombre maximun de zone que peut posseder un capteur
- `-mintmp <int>` correspond au nombre minimum de temps d'activation d'un capteur
- `-minzone <int>` correspond au nombre minimum de zone que peut posseder un capteur

## Partie 2: construction des configurations élémentaires

Le fichier `config-solver.py` permet de trouver les differentes configurations. Deux algorithme sont disponible: un algorithme recursif qui permet de trouver toutes les configurations mais qui demande beaucoup de calcul. Le deuxieme algorithme permet de trouver un certain nombre de configuration elementaire de maniere aleatoire.

### arguments

Ce script prend en argument un fichier generé par `json-gen.py`.

Argument optionelles:

- `-algoalea <bool>` permet d'utiliser l'algorithme aleatoire pour les fichier avec beaucoup de donnees
- `-nbconfig <int>` cette option limitte le nombre de configuration, les different algoritme va tout faire pour s'en raprocher

## Partie 3: ecriture et resolution du programe lineaire

Le fichier `lp-gen.py` permet de generer un le fichier lp.

    $ lp-gen.py exemple.json > exemple.lp

Une fois le fichier lp generer on resoud le probleme avec **glpk**:

    $ glpsol --cpxlp exemple.lp -o exemple.sol

**note:** les fichiers `exemple.*` corresponde à l'exemple dans l'[énnoncé](https://raw.github.com/Ricain/zone/master/projet-plcapteurs.pdf) du projet. 

### arguments

Afin d'utiliser des configurations pour generer le fichier lp, ce script prend les même argument que `config-solver.py`.
