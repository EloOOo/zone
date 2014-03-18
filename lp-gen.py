#!/usr/bin/env python

import sys

from lib import file_to_dict,configuration,inconu

const = {}
const["nbconfig"]  = 0     # nombre de configuration a obtenir, zero pour obtenir toute les configurations
const["algoalea"]  = False # algorithme aloeatoire pour trouver les configurations, bien pour les gros fichiers 

if len(sys.argv)<2:
	print "usage: filename "
	for x,y in const.iteritems():
		if type(y) is int:
			print "[-" + x + " <int>]"
		elif type(y) is bool:
			print "[-" + x + " <bool>]"
		else :
			print "[-" + x + " <float>]"
	exit(1)

for arg in sys.argv[2:]:
	if arg[:1]=="-" :
		if arg[1:] in const:
			if type(const[arg[1:]]) is int:
				const[arg[1:]] = int(sys.argv[sys.argv.index(arg)+1])
			elif type(const[arg[1:]]) is bool:
				const[arg[1:]] = bool(sys.argv[sys.argv.index(arg)+1])
			else :
				const[arg[1:]] = float(sys.argv[sys.argv.index(arg)+1])
		else :
			print arg[1:] + ": illegal option"
			exit(2)

tree = file_to_dict(sys.argv[1])
all_config = configuration(tree,const["nbconfig"],const["algoalea"])

capteur_used = []
for config in all_config:
	for capteur in config:
		if capteur not in capteur_used:
			capteur_used.append(capteur)

sys.stdout.write("\\ configurations: \n")
for l in range(len(all_config)):
	sys.stdout.write("\\  " + inconu(l) + " = " + str(all_config[l]) + "\n")

sys.stdout.write("\nMaximize a")
for l in range(1,len(all_config)):
	sys.stdout.write(" + " + inconu(l))

sys.stdout.write("\n\nSubject To\n\n")

for capteur in capteur_used:
	signe = " "
	for config in all_config:
		if capteur in config:
			sys.stdout.write(signe + inconu(all_config.index(config)))
			signe = " + "
		else:
			sys.stdout.write("    ")
	sys.stdout.write(" <= " + str(tree[capteur]["tmp"]) + "\n")

sys.stdout.write("\nEND\n")
