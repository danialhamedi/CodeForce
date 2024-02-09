num_of_tests = int(input())
for i in range(num_of_tests):
	lenght, maximum_water = map(int, input().split())
	coral = map(int,input().split())
	occurrences = {}
	for column in coral:
		occurrences[column] = occurrences.get(column,0) + 1
	
