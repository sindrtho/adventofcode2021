'''
		Calculate (x, y) position and multiply the coordinates
'''

def forward(coordinate, value):
	coordinate[0] += value
	coordinate[1] += value*coordinate[2]

def down(coordinate, value):
	coordinate[2] += value

def up(coordinate, value):
	coordinate[2] -= value

actions = {
	'forward': forward,
	'down': down,
	'up': up
}

with open('input.txt', 'r') as file:
	coordinates = [0, 0, 0]

	line = file.readline()

	while line:
		action, value = line.split()
		actions[action](coordinates, int(value))
		line = file.readline()

	print(coordinates)
	print(coordinates[0]*coordinates[1])