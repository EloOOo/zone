#!/usr/bin/env python

import sys

from lib import configuration,file_to_dict

const = {}
const["nbconfig"]  = 0     # nombre de configuration a obtenir, zero pour obtenir toute les configurations
const["algoalea"]  = False # algorithme aleatoire pour trouver les configuration, bien pour les gros fichiers 

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

print "\n".join([str(x) for x in configuration(file_to_dict(sys.argv[1]),const["nbconfig"],const["algoalea"])])