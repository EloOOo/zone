#!/usr/bin/env python

import json

# prend le nom d'un fichier et renvoie le dictionnaire correspondant
def loadfile(filename):
	with open(filename) as content:
		return json.loads(content.read())