#!/usr/bin/env python

import random
import json
import sys

const = {}
const["nbcapteur"]  = 10    # nombre de capteurs
const["minzone"]    = 1     # nombre minimun de zone par capteur
const["maxzone"]    = 4     # nombre maximum de zone par capteur
const["zonecoef"]   = .84   # attribution de zone deja cree 0 < const["zonecoef"] <= 1 attribution de nouvelle zone
const["mintmp"]     = 2     # temps de vie minimum d'un capteur
const["maxtmp"]     = 10    # temps de vie maximun d'un capteur
const["seed"]       = 0     # graine du generateur de nombre aleatoire, zero pour choisi aleatoirement

#test nombre arguments
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

if const["seed"] == 0:
	const["seed"] = random.randint(0,sys.maxint)
rand = random.Random(const["seed"])
print "seed: " + str(const["seed"])

zone = 0
capteur = {}
for t in range(const["nbcapteur"]):
	tmp = rand.randint(const["mintmp"],const["maxtmp"])
	localzone = []
	for _ in range(rand.randint(const["minzone"],const["maxzone"])):
		toadd  = -1
		while toadd in localzone or toadd==-1 :
			if rand.random()<const["zonecoef"] and zone>=const["maxzone"] :
				toadd = rand.randint(1,zone)	
			else :
				zone += 1
				toadd = zone
		localzone.append(toadd)
	capteur[t+1] = {"tmp":tmp,"zone":localzone}

print str(len(capteur)) + " capteurs cree"
print str(zone) + " zones cree"

save = open(sys.argv[1], "w")
save.write(json.dumps(capteur,indent=4))
save.close() 

print "resultat ecrit dans " + sys.argv[1]
