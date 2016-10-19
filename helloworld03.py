import random
import sys
import os

pi_tuple = (3, 1, 4, 1, 5, 9)

new_tuple = list(pi_tuple)  # converts tuple to a list
new_list = tuple(new_tuple)

len(new_tuple); min(new_tuple); max(new_tuple)

super_villains = {'Fiddler': 'Isaac',
	'Captain Cold': 'leonard'
}

print(super_villains['Captain Cold'])

del super_villains['Fiddler']

super_villains['Fiddler'] = 'new Fiddler'

print(len(super_villains))
print(super_villains.get('Fiddler'))

print(super_villains.keys())

print(super_villains.values())
