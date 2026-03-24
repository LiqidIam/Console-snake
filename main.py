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
		self.zones = []

	def update(self, player):
		# food spawn
		pass

	def render(self, player):
		output = ''
		for y in range(self.height):
			for x in range(self.width):
				if x == player.x and y == player.y:
					output += '@ '
				else:
					output += f'{self.tiles[x][y]} '
			output += '\n'
		return output

class Player(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.direction_list = ['North', 'South', 'East', 'West']
		self.direction = self.direction_list[0]

	def rotate(self, rotation:str, world):
		match rotation:
			case 'up':
				if self.direction != 'South':
					self.direction = 'North'
			case 'down':
				if self.direction != 'North':
					self.direction = 'South'
			case 'right':
				if self.direction != 'West':
					self.direction = 'East'
			case 'left':
				if self.direction != 'East':
					self.direction = 'West'

	def move(self, world):
		match self.direction:
			case 'North': self.y = max(0, min(self.y - 1, world.height - 1))
			case 'South': self.y = max(0, min(self.y + 1, world.height - 1))
			case 'East': self.x = max(0, min(self.x + 1, world.width - 1))
			case 'West': self.x = max(0, min(self.x - 1, world.width - 1))

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

# ========================================
# Main Game Cycle
# ========================================
isPlaying = True

def main():
	# Инициализация всяких штук
	world = World()
	player = Player(1, 3)

	# world.generate()

	# Основной цикл
	while isPlaying == True:
		handle_input(player, world)
		player.move(world)
		world.update(player)
		print('\n'*25 + f'{world.render(player)}')
		# world.render(player)

		time.sleep(0.25)

# Запуск игры
if __name__ == '__main__':
	main()