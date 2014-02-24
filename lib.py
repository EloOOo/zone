#!/usr/bin/env python

import json
import networkx as nx

# prend le nom d'un fichier et renvoie le graph correspondant
def loadfile(filename):
	graph = nx.Graph()
	with open(filename) as content:
		edges = {}
		for key,value in json.loads(content.read()).iteritems():
			graph.add_nodes_from(value["zone"])
			print value["zone"]
			if len(value["zone"])==1:
				graph.add_edge(value["zone"][0],0,capteur=int(key),tmp=int(value["tmp"]))
				continue
			for x in value["zone"]:
				for y in range(value["zone"].index(x)+1,len(value["zone"])):
					graph.add_edge(x,value["zone"][y],capteur=int(key),tmp=int(value["tmp"])) 
	return graph