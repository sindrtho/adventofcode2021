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
	
	o2 = numbers
	index = 0
	while len(o2) > 1:
		print(o2)
		if sum(o2[:, index]) >= len(o2) / 2:
			o2 = o2[o2[:, index] == 1]
		else:
			o2 = o2[o2[:, index] == 0]
		index += 1

	co2 = numbers
	index = 0
	while len(co2) > 1:
		if sum(co2[:, index]) >= len(co2) / 2.0:
			co2 = co2[co2[:, index] == 0]
		else:
			co2 = co2[co2[:, index] == 1]
		index += 1

	o2_value = int(''.join([str(x) for x in o2[0]]), 2)
	co2_value = int(''.join([str(x) for x in co2[0]]), 2)
	print(o2_value)
	print(co2_value)
	print(o2_value*co2_value)