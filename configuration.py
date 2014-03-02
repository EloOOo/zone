#!/usr/bin/env python

import sys

execfile("lib.py")

if len(sys.argv)<2:
	print "usage: filename"
	exit(1)

print "\n".join([str(x) for x in configuration(inverse(file_to_dict(sys.argv[1])))])