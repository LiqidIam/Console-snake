import time
import random
import platform
if platform.system() == 'Windows':
	import msvcrt
	def get_key():
		return msvcrt.getch().decode() if msvcrt.kbhit() else None
from config import *
from colorama import init as colorama_init
colorama_init(autoreset=True)

# ========================================
# Classes
# ========================================
class World(object):
	def __init__(self, width=20, height=20):
		self.width = width
		self.height = height
		self.tiles = [[DEFAULT_TILE for _ in range(width)] for _ in range(height)]
		self.food = []

	def update(self, player):
		# Food spawn
		if len(self.food) < AMOUNT_OF_FOOD:
			new_food = []
			while True:
				x = random.randint(0, self.width-1)
				y = random.randint(0, self.height-1)
				new_food = [x, y]
				if new_food not in player.body and new_food not in self.food: break
			self.food.append(new_food)

		# Death check
		if player.body[-1] in player.body[:-1]:
			game_quit()

	def render(self, player, world):
		output = []
		for y in range(self.height):
			row = ' '
			for x in range(self.width):
				pos = [x, y]
				if pos in player.body:
					if pos == player.body[-1]:
						row += PLAYER_HEAD
					else:
						row += PLAYER_TAIL
				elif pos in world.food:
					row += FOOD
				else:
					row += f'{self.tiles[x][y]}'
			output.append(row)

		menu = [f'SCORE: {player.score}',
				'===============',
				f'Amount of food: {AMOUNT_OF_FOOD}',
				f'Game speed: {GAME_SPEED}x',
				'===============',
				f'Theme: {theme}']

		full_screen = []
		for i, row in enumerate(output):
			menu_row = menu[i] if i < len(menu) else ' '
			full_screen.append(row + ' | ' + menu_row)
		return '\n'.join(full_screen)

class Player(object):
	def __init__(self, x, y):
		self.body = [[x, y-1], [x, y]]
		self.direction = 'North'
		self.score = 0

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
			case 'South':
				new_y = max(0, min(y + 1, world.height - 1))
				new_head = [x, new_y]
			case 'East':
				new_x = max(0, min(x + 1, world.width - 1))
				new_head = [new_x, y]
			case 'West':
				new_x = max(0, min(x - 1, world.width - 1))
				new_head = [new_x, y]
		self.body.append(new_head)

	def eat(self, world):
		if self.body[-1] in world.food:
			world.food.pop(world.food.index(self.body[-1]))
			self.score += 1
		else:
			self.body.pop(0)

# ========================================
# Functions
# ========================================
def handle_input(player, world):
	key = get_key()	# Нажатие клавиши
	if key == KEY_UP: player.rotate('up', world)
	elif key == KEY_DOWN: player.rotate('down', world)
	elif key == KEY_RIGHT: player.rotate('right', world)
	elif key == KEY_LEFT: player.rotate('left', world)
	elif key == KEY_QUIT: game_quit()

def game_quit():
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
	player = Player(world.width//2, world.height//2)

	# world.generate()

	# Основной цикл
	while isPlaying == True:
		handle_input(player, world)
		player.move(world)
		player.eat(world)
		world.update(player)
		print(f'\n{world.render(player, world)}'+'\n'*42, end='')

		time.sleep(0.25 / GAME_SPEED)

# Запуск игры
if __name__ == '__main__':
	main()