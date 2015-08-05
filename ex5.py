#!/usr/bin/env python
# encoding: utf-8

zzm_name = 'Zhaozm'
zzm_age = 35  # not a line
inches_to_cm = 2.54
zzm_height = 74 * inches_to_cm  # cm
pounds_to_kg = 0.45359237
zzm_weight = 180 * pounds_to_kg  # kg
zzm_eyes = 'Blue'
zzm_teeth = 'White'
zzm_hair = 'Brown'

print "Let's talk about %r." % zzm_name
print "He's %r cm tall." % zzm_height
print "He's %d kg heavy." % zzm_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (zzm_eyes, zzm_hair)
print "His teeth are usually %s depending on the coffee." % zzm_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    zzm_age, zzm_height, zzm_weight, zzm_age + zzm_height + zzm_weight)
