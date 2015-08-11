#!/usr/bin/env python
# encoding: utf-8

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncatin the file. GOodBye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write('%r\n' % line1)
target.write('%r\n' % line2)
target.write('%r\n' % line3)
print "And finally, we close it."
target.close()

f = open(filename)
print f.read()
