test = int(input())
for i in range(test):
	string = input()
	possible_ways = {'abc', 'cba', 'bac', 'acb'}
	if string in possible_ways:
		print("Yes")
	else:
		print("NO")