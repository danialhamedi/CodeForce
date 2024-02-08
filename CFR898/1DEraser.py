num_of_test = int(input())

for _ in range(num_of_test):
	storage = {}
	current_longest = 0
	n, k = map(int,input().split(" "))
	string = list(input())
	pointer = 0
	res = 0
	while pointer < n:
		if string[pointer] == 'B':
			pointer += k
			res += 1
		else:
			pointer += 1
	print(res)

