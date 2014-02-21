#!/usr/bin/env python

import random
import json

NB_CAPTEURS  = 100    # nombre de capteurs
MIN_ZONES    = 1      # nombre minimun de zone par capteur
MAX_ZONES    = 10     # nombre maximum de zone par capteur
ZONE_COEF    = .84    # attribution de zone deja cree 0 < ZONE_COEF <= 1 attribution de nouvelle zone
MIN_VIE      = 1      # temps de vie minimum d'un capteur
MAX_VIE      = 10     # temps de bie maximun d'un capteur

zone = 0
capteur = []
for _ in range(NB_CAPTEURS):
	vie = random.randint(MIN_VIE,MAX_VIE)
	localzone = []
	for _ in range(random.randint(MIN_ZONES,MAX_ZONES)):
		toadd  = -1
		while toadd in localzone or toadd==-1 :
			if random.random()<ZONE_COEF and zone>0 :
				toadd = random.randint(1,zone)	
			else :
				zone += 1
				toadd = zone
		localzone.append(toadd)
	capteur.append((vie,localzone))

print str(len(capteur)) + " capteurs cree"
print str(zone) + " zones cree" 