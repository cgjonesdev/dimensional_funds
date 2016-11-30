import string

temp = dict(zip(string.letters[:26], range(1,27)))
temp.update(
	dict(zip(string.punctuation,
	[int(a[0]) for a in zip('0'*len(string.punctuation))])))
temp.update({' ':0})

result = sorted([(len(a), a) for a in [a[:-1] for a in open(
	'american-words.80').readlines()] if sum([temp[b] for b in a]) == 100])

if __name__ == '__main__':
	for r in result: print(r[1])
