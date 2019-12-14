lines = open("./emoji_unicode.txt").read().split('\n')
j = 0
for i in lines:
	if 0 == j % 32:
		print('\n')
	print(chr(int(i, base=16)), end='  ')
	j += 1
print('\n')
