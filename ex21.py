#!/usr/bin/env python
# encoding: utf-8


def add(a, b):
    print "adding %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "subtracting %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "multiplying %d * %d" % (a, b)
    return a * b


def div(a, b):
    print "diving %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = div(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = multiply(age, subtract(height, add(weight, div(iq, 2))))
print "That becomes: ", what, "can you do it by hand?"
