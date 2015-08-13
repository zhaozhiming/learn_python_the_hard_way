#!/usr/bin/env python
# encoding: utf-8

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New Yorkk'
cities['OR'] = 'Portland'

print "-" * 10
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is:", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
    print '%s is abbreviation %s' % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviation %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
state = states.get("Texes", None)

if not state:
    print "sorry, no texas"

city = cities.get("TX", "Does not exist")
print "The city for the state 'TX' is: %s" % city
