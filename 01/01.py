'''
Sonar Sweep

For n lines of input, calculate the number of lines where the vale is higher then the previous line
'''

with open('input.txt', 'r') as file:
	prev = float('inf')
	res = 0

	line = file.readline()
	while line:
		current = int(line)

		res += int(current > prev)
		prev = current
		line = file.readline()

	print(res)