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

	def update(self):
		# food spawn
		# player move
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
		self.direction_list = ['North', 'East', 'South', 'West']
		self.direction = self.direction_list[0]

	def move(self, dx, dy, world):
		self.x = max(0, min(self.x + dx, world.width - 1))
		self.y = max(0, min(self.y + dy, world.height - 1))

# class Food(object):
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y

# ========================================
# Functions
# ========================================
def handle_input(player, world):
	global isPlaying
	key = get_key()	# Нажатие клавиши
	if key == KEY_UP: player.move(0, -1, world)		# Вверх
	elif key == KEY_DOWN: player.move(0, 1, world)	# Вниз
	elif key == KEY_LEFT: player.move(-1, 0, world)	# Влево
	elif key == KEY_RIGHT: player.move(1, 0, world)	# Вправо
	elif key == KEY_QUIT:
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
		world.update()
		print('\n'*25 + f'{world.render(player)}')
		# world.render(player)

		time.sleep(0.25)

# Запуск игры
if __name__ == '__main__':
	main()