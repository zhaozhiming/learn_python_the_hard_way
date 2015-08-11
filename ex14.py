#!/usr/bin/env python
# encoding: utf-8

from sys import argv

script, user_name, age = argv
prompt = '% '

print "Hi %s, you're %r age, I'm the %s script." % (user_name, age, script)
print "I'd like to ask you a few questions."
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer)
