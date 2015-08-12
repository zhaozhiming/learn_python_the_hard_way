#!/usr/bin/env python
# encoding: utf-8


def loop_while(count, step=1):
    # i = 0
    numbers = []
    for i in range(0, count, step):
        print "At the top i is %d" % i
        numbers.append(i)
        # i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers


numbers = loop_while(5, 2)
print "The numbers: "

for num in numbers:
    print num
