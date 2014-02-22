#!/usr/bin/env python

import random
import json
import sys

NB_CAPTEURS  = 100    # nombre de capteurs
MIN_ZONES    = 1      # nombre minimun de zone par capteur
MAX_ZONES    = 10     # nombre maximum de zone par capteur
ZONE_COEF    = .84    # attribution de zone deja cree 0 < ZONE_COEF <= 1 attribution de nouvelle zone
MIN_TMP      = 1      # temps de vie minimum d'un capteur
MAX_TMP      = 10     # temps de bie maximun d'un capteur

if len(sys.argv)<2:
	print "usage: filename [seed]"
	exit(1)

if len(sys.argv)>=3 :
	seed = int("0" + sys.argv[2])
else : 
	seed = random.randint(sys.maxint)
rand = random.Random(seed)
print "seed: " + str(seed)

zone = 0
capteur = {}
for t in range(NB_CAPTEURS):
	tmp = rand.randint(MIN_TMP,MAX_TMP)
	localzone = []
	for _ in range(rand.randint(MIN_ZONES,MAX_ZONES)):
		toadd  = -1
		while toadd in localzone or toadd==-1 :
			if rand.random()<ZONE_COEF and zone>=MAX_ZONES :
				toadd = rand.randint(1,zone)	
			else :
				zone += 1
				toadd = zone
		localzone.append(toadd)
	capteur[t+1] = {"tmp":tmp,"zone":localzone}

print str(len(capteur)) + " capteurs cree"
print str(zone) + " zones cree"

save = open(sys.argv[1], "w")
save.write("// seed = " + str(seed) + "\n\n" +json.dumps(capteur,indent=4))
save.close() 

print "resultat ecrit dans " + sys.argv[1]