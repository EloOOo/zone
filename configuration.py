#!/usr/bin/env python

import sys

execfile("lib.py")

const = {}
const["minconfig"]  = 0    # nombre minumun de config a obtenir, zero si pas de minimum

if len(sys.argv)<2:
	print "usage: filename "
	for x,y in const.iteritems():
		if type(y) is int:
			print "[-" + x + " <int>]"
		else :
			print "[-" + x + " <float>]"
	exit(1)

for arg in sys.argv[2:]:
	if arg[:1]=="-" :
		if arg[1:] in const:
			if type(const[arg[1:]]) is int:
				const[arg[1:]] = int(sys.argv[sys.argv.index(arg)+1])
			else :
				const[arg[1:]] = float(sys.argv[sys.argv.index(arg)+1])
		else :
			print arg[1:] + ": illegal option"
			exit(2)

print "\n".join([str(x) for x in configuration(inverse(file_to_dict(sys.argv[1])),const["minconfig"])])