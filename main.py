import time
import random
import platform
if platform.system() == 'Windows':
	import msvcrt
	def get_key():
		return msvcrt.getch().decode() if msvcrt.kbhit() else None
from config import *

# ========================================
# Classes
# ========================================
class World(object):
	def __init__(self, width=20, height=20):
		self.width = width
		self.height = height
		self.tiles = [['.' for _ in range(width)] for _ in range(height)]

	def update(self, player):
		# food spawn
		pass

	def render(self, player):
		output = ''
		for y in range(self.height):
			for x in range(self.width):
				pos = [x,y]
				# print(f'{pos} in {player.body}')
				if pos in player.body:
					if pos == player.body[-1]:
						output += '@ '
					else:
						output += 'O '
				else:
					output += f'{self.tiles[x][y]} '
			output += '\n'
		return output

class Player(object):
	def __init__(self, x, y):
		self.body = [[x,y-1], [x,y]]
		self.direction = 'North'

	def rotate(self, rotation:str, world):
		match rotation:
			case 'up':
				self.direction = 'North' if self.direction != 'South' else 'South'
			case 'down':
				self.direction = 'South' if self.direction != 'North' else 'North'
			case 'right':
				self.direction = 'East' if self.direction != 'West' else 'West'
			case 'left':
				self.direction = 'West' if self.direction != 'East' else 'East'

	def move(self, world):
		x = self.body[-1][0]
		y = self.body[-1][1]
		match self.direction:
			case 'North':
				new_y = max(0, min(y - 1, world.height - 1))
				new_head = [x, new_y]
				self.body.append(new_head)
			case 'South':
				new_y = max(0, min(y + 1, world.height - 1))
				new_head = [x, new_y]
				self.body.append(new_head)
			case 'East':
				new_x = max(0, min(x + 1, world.width - 1))
				new_head = [new_x, y]
				self.body.append(new_head)
			case 'West':
				new_x = max(0, min(x - 1, world.width - 1))
				new_head = [new_x, y]
				self.body.append(new_head)

# class Food(object):
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y

# ========================================
# Functions
# ========================================
def handle_input(player, world):
	key = get_key()	# Нажатие клавиши
	if key == KEY_UP: player.rotate('up', world)
	elif key == KEY_DOWN: player.rotate('down', world)
	elif key == KEY_RIGHT: player.rotate('right', world)
	elif key == KEY_LEFT: player.rotate('left', world)
	elif key == KEY_QUIT:
		global isPlaying
		isPlaying = False
		print("\nВыход из игры")
		print(player.body)

# ========================================
# Main Game Cycle
# ========================================
isPlaying = True

def main():
	# Инициализация всяких штук
	world = World()
	player = Player(9, 9)

	# world.generate()

	# Основной цикл
	while isPlaying == True:
		handle_input(player, world)
		player.move(world)
		world.update(player)
		print(f'\n{world.render(player)}'+'\n'*42)

		time.sleep(0.25)

# Запуск игры
if __name__ == '__main__':
	main()