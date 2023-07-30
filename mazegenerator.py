import random

WALL = 1
EMPTY = 0

def check(maze, width, height):
	start_cell = width * height - width
	end_cell = width - 1
	temp = [0] * width * height
	temp[start_cell] = maze[start_cell] == EMPTY
	end = False
	while not end:
		end = True
		for y in range(height):
			for x in range(width):
				if temp[x + y * width] == 1:
					if y > 0 and maze[x + (y-1) * width] == EMPTY and temp[x + (y-1) * width] == 0:
						temp[x + (y-1) * width] = 1
						end = False
					if y < height - 1 and maze[x + (y+1) * width] == EMPTY and temp[x + (y+1) * width] == 0:
						temp[x + (y+1) * width] = 1
						end = False
					if x > 0 and maze[(x-1) + y * width] == EMPTY and temp[(x-1) + y * width] == 0:
						temp[(x-1) + y * width] = 1
						end = False
					if x < width - 1 and maze[(x+1) + y * width] == EMPTY and temp[(x+1) + y * width] == 0:
						temp[(x+1) + y * width] = 1
						end = False

	return temp[end_cell] == 1

def generate(width, height, singlepath=False, logging=True):
	maze = [EMPTY] * width * height

	cells = []
	temp = []
	for i in range(width * height):
		temp.append(i)
	
	for i in range(width * height):
		cells.append(temp.pop(random.randint(0, len(temp) - 1)))
	
	count = 0
	for cell in cells:
		if logging:
			print("Generating: " + str(count) + " / " + str(width * height))
			count += 1
		
		maze[cell] = WALL
		if not check(maze, width, height):
			maze[cell] = EMPTY

	if not singlepath:
		for y in range(height):
			for i in range(width // 3):
				maze[random.randint(0, width - 1) + y * width] = EMPTY

	for y in range(height):
		for x in range(width):
			if maze[x + y * width] == WALL:
				print("#", end="")
			else:
				print(" ", end="")
		
		print()

generate(25, 20, False, True)

