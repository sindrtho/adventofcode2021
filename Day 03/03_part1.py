import numpy as np
import re

with open('input.txt', 'r') as file:
	numbers = []
	line = file.readline()
	while line:
		n = re.findall('\d', line)
		numbers.append([int(x) for x in n])

		line = file.readline()

	numbers = np.array(numbers)
	
	gamma = int(''.join(['1' if sum(numbers[:, i]) >= len(numbers)/2 else '0' for i in range(len(numbers[0]))]), 2)
	epsilon = int(''.join(['0' if sum(numbers[:, i]) >= len(numbers)/2 else '1' for i in range(len(numbers[0]))]), 2)

	print(gamma)
	print(epsilon)
	print(gamma*epsilon)