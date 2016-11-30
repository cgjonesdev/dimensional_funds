from collections import Counter
from random import choice

animals = (['cat'],['dog'],['horse'],['bird'],['cow'],['elephant'],['moose'])
l = []
for a in animals: l.extend(list(a)*choice(range(25)))
c = Counter(l)
for s in sorted([(v, k) for k, v in c.items()]): print s
print
for s in sorted([(v, k) for k, v in c.items()], reverse=True): print s
