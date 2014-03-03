#!/usr/bin/env python

import json
import networkx as nx

# prend le nom d'un fichier et renvoie le graph correspondant
def file_to_graph(filename):
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

# prend le nom d'un fichier et renvoie le dictionnaire correspondant
def file_to_dict(filename):
	with open(filename) as content:
		return unicode_to_ascii(json.loads(content.read()))

# convert the argument to asccii
def unicode_to_ascii(input):
	if isinstance(input, dict):
		return {unicode_to_ascii(key):unicode_to_ascii(value) for key,value in input.iteritems()}
	elif isinstance(input, list):
		return [unicode_to_ascii(element) for element in input]
	elif isinstance(input, unicode):
		return unicode_to_ascii(input.encode('utf-8'))
	elif isinstance(input, str) and input.isdigit():
		return int(input)
	else:
		return input

# renvoie toute les configurations, prend en parametre un dictionnaire de type inverse
def configuration(datas,min):
	all = []
	vers(datas,[],1,all,min)
	return all

# parcour des donnes et place toute les confgurations dans data
def vers(tree,config,level,all,min):
	if len(all)>=min and min!=0:
		return
	if len(tree)<level:
		for x in all:
			if config_equal(config,x):
				return
		all.append(config)
		return 
	for x in tree[level]:
		inter = list(config)
		if x not in config:
			inter.append(x)
		vers(tree, inter, level+1, all, min)

# renvoie vrai si les deux configuration sont eguale
def config_equal(config1,config2):
	if len(config1)!=len(config2):
		return False
	for x in config1:
		if x not in config2:
			return False
	return True

# renvoi le dictionnaire inverse: capteur en fonction des zonne: {zone:[capteur,capteur,etc],etc}
def inverse(datas):
	inverse = {}
	for capteur,all in datas.iteritems():
		for x in all["zone"]:
			if x in inverse:
				inverse[x].append(capteur)
			else:
				inverse[x] = [capteur]
	return inverse
