#!/usr/bin/env python
# encoding: utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print raw_input("Ready, hit RETURN to continue, CTRL-C to abort.")

open(to_file, 'w').write(indata)

print "Alright, all done."

print "To file content:"
f = open(to_file)
print f.read()
